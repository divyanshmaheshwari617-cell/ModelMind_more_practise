
"""
ModelMind Docker Judge

Development-only implementation.

Requires Docker Desktop with Linux containers.

Not certified for public multi-tenant execution.
"""

import json
import shutil
import subprocess
import tempfile
import time

from pathlib import Path


IMAGE = "modelmind-judge:local"

RESULT_MARKER = "__MODELMIND_RESULT__"


def run_in_docker(
    runner_source: str,
    test_cases_path: Path,
    mode: str
):
    if mode not in ("run", "submit"):
        raise ValueError(
            "Mode must be run or submit"
        )

    if shutil.which("docker") is None:
        raise RuntimeError(
            "Docker is not installed or not on PATH"
        )

    with tempfile.TemporaryDirectory(
        prefix="modelmind_"
    ) as folder:

        work = Path(folder)

        (work / "runner.py").write_text(
            runner_source,
            encoding="utf-8"
        )

        shutil.copyfile(
            test_cases_path,
            work / "test_cases.py"
        )

        command = [
            "docker",
            "run",
            "--rm",
            "--network", "none",
            "--read-only",
            "--cap-drop", "ALL",
            "--security-opt",
            "no-new-privileges",
            "--pids-limit", "64",
            "--memory", "768m",
            "--cpus", "1",
            "--user", "65534:65534",
            "--tmpfs",
            "/tmp:rw,noexec,nosuid,size=64m",
            "--mount",
            (
                f"type=bind,"
                f"src={work.resolve()},"
                f"dst=/work,readonly"
            ),
            "--workdir", "/tmp",
            IMAGE,
            "python",
            "-I",
            "/work/runner.py"
        ]

        start = time.perf_counter()

        try:
            completed = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=15,
                check=False
            )

        except subprocess.TimeoutExpired:
            raise RuntimeError(
                "Docker execution exceeded its time limit"
            )

        duration = round(
            (time.perf_counter() - start) * 1000
        )

        matching = [
            line
            for line in completed.stdout.splitlines()
            if line.startswith(RESULT_MARKER)
        ]

        if not matching:
            raise RuntimeError(
                "Judge failed: "
                + completed.stderr[-500:]
            )

        result = json.loads(
            matching[-1][len(RESULT_MARKER):]
        )

        if mode == "submit":
            for i, test in enumerate(
                result.get("tests", [])
            ):
                if i >= 2:
                    test["name"] = (
                        f"Hidden test {i - 1}"
                    )
                    test.pop("error", None)

        result.update({
            "tests_available": True,
            "stdout": "",
            "stderr": "",
            "execution_time_ms": duration
        })

        return result
