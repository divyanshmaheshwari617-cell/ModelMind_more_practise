
import os
import urllib.request
import urllib.error
import json

JUPYTER_URL = os.getenv(
    "JUPYTER_SERVER_URL",
    "http://127.0.0.1:8888"
).rstrip("/")

JUPYTER_TOKEN = os.getenv(
    "JUPYTER_TOKEN", ""
)


def check_jupyter():
    url = f"{JUPYTER_URL}/api/kernelspecs"

    request = urllib.request.Request(
        url,
        headers={
            "Authorization": f"token {JUPYTER_TOKEN}"
        } if JUPYTER_TOKEN else {}
    )

    try:
        with urllib.request.urlopen(
            request, timeout=5
        ) as response:
            data = json.load(response)

        print("Jupyter connection successful!")
        print("Available kernels:")

        for name in data.get("kernelspecs", {}):
            print("-", name)

        return True

    except urllib.error.HTTPError as error:
        print("Jupyter HTTP error:", error.code)
        return False

    except Exception as error:
        print("Connection failed:", error)
        return False


if __name__ == "__main__":
    check_jupyter()
