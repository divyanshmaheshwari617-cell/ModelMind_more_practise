"""Local-only Jupyter Server integration for ModelMind.

Notebook experimentation is NOT a grading/sandbox service. Do not expose this
router to the public Internet or to untrusted users. Uses fresh kernel per call.
"""
import base64
import json
import os
import time
import uuid
from urllib.parse import urlparse, quote
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(prefix="/api/notebook", tags=["Local Jupyter"])

class CellRequest(BaseModel):
    question_id: str = Field(default="", max_length=128)
    code: str = Field(min_length=1, max_length=20000)


def _config():
    if os.getenv("MODELMIND_ENABLE_LOCAL_JUPYTER", "false").lower() != "true":
        raise HTTPException(503, "Local Jupyter integration is disabled")
    url = os.getenv("JUPYTER_SERVER_URL", "http://127.0.0.1:8888").rstrip("/")
    parsed = urlparse(url)
    if parsed.scheme != "http" or parsed.hostname not in ("localhost", "127.0.0.1", "::1"):
        raise HTTPException(503, "Only localhost Jupyter servers are allowed")
    token = os.getenv("JUPYTER_TOKEN", "")
    if not token:
        raise HTTPException(503, "Set JUPYTER_TOKEN in backend environment")
    return url, token


def _rest(method, endpoint, payload=None):
    url, token = _config()
    body = json.dumps(payload).encode() if payload is not None else None
    req = Request(url + endpoint, data=body, method=method,
                  headers={"Authorization": "token " + token,
                           "Content-Type": "application/json"})
    try:
        with urlopen(req, timeout=8) as resp:
            data = resp.read()
            return json.loads(data) if data else None
    except (HTTPError, URLError, TimeoutError) as exc:
        raise HTTPException(502, "Cannot communicate with local Jupyter Server: " + str(exc)) from exc


@router.get("/status")
def status():
    specs = _rest("GET", "/api/kernelspecs")
    return {"connected": True, "kernels": list(specs.get("kernelspecs", {}))}


@router.post("/execute")
def execute_cell(req: CellRequest):
    # Intentionally a single-use kernel; no cross-cell state and no hidden tests.
    try:
        import websocket  # pip install websocket-client
    except ImportError as exc:
        raise HTTPException(503, "Install websocket-client in the backend venv") from exc
    url, token = _config()
    kernelspec = os.getenv("JUPYTER_KERNEL_NAME", "python3")
    timeout = min(max(int(os.getenv("MODELMIND_CELL_TIMEOUT", "12")), 2), 30)
    kernel = _rest("POST", "/api/kernels", {"name": kernelspec})
    kid = kernel["id"]
    ws = None
    outputs = []
    stdout, stderr = [], []
    started = time.monotonic()
    try:
        address = url.replace("http://", "ws://", 1)
        ws = websocket.create_connection(
            f"{address}/api/kernels/{quote(kid)}/channels",
            timeout=2,
            header=[f"Authorization: token {token}"],
            origin="http://localhost",
        )
        msgid = uuid.uuid4().hex
        msg = {
            "header": {"msg_id": msgid, "username": "modelmind", "session": uuid.uuid4().hex,
                       "date": "", "msg_type": "execute_request", "version": "5.3"},
            "parent_header": {}, "metadata": {}, "channel": "shell",
            "content": {"code": req.code, "silent": False, "store_history": False,
                        "user_expressions": {}, "allow_stdin": False, "stop_on_error": True},
        }
        ws.send(json.dumps(msg))
        status_value = "timeout"
        while time.monotonic() - started < timeout:
            ws.settimeout(min(1.0, max(.1, timeout - (time.monotonic() - started))))
            try:
                data = json.loads(ws.recv())
            except websocket.WebSocketTimeoutException:
                continue
            if data.get("parent_header", {}).get("msg_id") != msgid:
                continue
            kind = data.get("msg_type", data.get("header", {}).get("msg_type"))
            content = data.get("content", {})
            if kind == "stream":
                (stderr if content.get("name") == "stderr" else stdout).append(str(content.get("text", "")))
            elif kind in ("display_data", "execute_result"):
                mime = content.get("data", {})
                if "image/png" in mime:
                    img = mime["image/png"]
                    if isinstance(img, str) and len(img) <= 4_000_000:
                        outputs.append({"type": "image/png", "data": img})
                if "text/plain" in mime:
                    outputs.append({"type": "text/plain", "data": str(mime["text/plain"])[:30000]})
            elif kind == "error":
                status_value = "error"
                stderr.append("\n".join(content.get("traceback", []))[-20000:])
            elif kind == "status" and content.get("execution_state") == "idle":
                if status_value != "error":
                    status_value = "success"
                break
        return {"status": status_value,
                "stdout": "".join(stdout)[:30000], "stderr": "".join(stderr)[:30000],
                "outputs": outputs[:10],
                "execution_time_ms": round((time.monotonic() - started) * 1000)}
    finally:
        if ws:
            ws.close()
        try:
            _rest("DELETE", f"/api/kernels/{quote(kid)}")
        except Exception:
            pass
