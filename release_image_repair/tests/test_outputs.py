import json
import subprocess
import time


def run(cmd: str) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, shell=True, text=True, capture_output=True)


def cleanup_server() -> None:
    subprocess.run("pkill -f 'uvicorn app:app' >/dev/null 2>&1 || true", shell=True, check=False)


def install_dependencies() -> subprocess.CompletedProcess:
    return run("cd /app/repo && python3 -m pip install --no-cache-dir -r service/requirements.txt")


def start_server() -> subprocess.Popen:
    return subprocess.Popen(
        "cd /app/repo && python3 -m uvicorn app:app --host 127.0.0.1 --port 18080",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def wait_for_health() -> str | None:
    for _ in range(20):
        response = run("curl -fsS http://127.0.0.1:18080/health")
        if response.returncode == 0:
            return response.stdout.strip()
        time.sleep(1)
    return None


def test_dependencies_install_from_project_requirements():
    result = install_dependencies()
    assert result.returncode == 0, (
        f"dependency install failed\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )


def test_service_starts_from_repo_root_entrypoint():
    cleanup_server()
    proc = None
    try:
        install = install_dependencies()
        assert install.returncode == 0, (
            f"dependency install failed\nSTDOUT:\n{install.stdout}\nSTDERR:\n{install.stderr}"
        )

        proc = start_server()
        body = wait_for_health()
        assert body is not None, "service did not start successfully from repo root entrypoint"
    finally:
        cleanup_server()
        if proc is not None:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except Exception:
                pass


def test_health_endpoint_returns_expected_payload():
    cleanup_server()
    proc = None
    try:
        install = install_dependencies()
        assert install.returncode == 0, (
            f"dependency install failed\nSTDOUT:\n{install.stdout}\nSTDERR:\n{install.stderr}"
        )

        proc = start_server()
        body = wait_for_health()
        assert body is not None, "/health endpoint never became available"

        payload = json.loads(body)
        assert payload == {"status": "ok", "service": "release-api"}
    finally:
        cleanup_server()
        if proc is not None:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except Exception:
                pass


def test_root_endpoint_still_returns_expected_payload():
    cleanup_server()
    proc = None
    try:
        install = install_dependencies()
        assert install.returncode == 0, (
            f"dependency install failed\nSTDOUT:\n{install.stdout}\nSTDERR:\n{install.stderr}"
        )

        proc = start_server()

        body = None
        for _ in range(20):
            response = run("curl -fsS http://127.0.0.1:18080/")
            if response.returncode == 0:
                body = response.stdout.strip()
                break
            time.sleep(1)

        assert body is not None, "root endpoint never became available"

        payload = json.loads(body)
        assert payload == {"message": "release api"}
    finally:
        cleanup_server()
        if proc is not None:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except Exception:
                pass