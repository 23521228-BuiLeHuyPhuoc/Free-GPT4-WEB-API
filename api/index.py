import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))


def load_local_env(path: Path) -> None:
    if not path.exists():
        return

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


load_local_env(ROOT_DIR / ".env")

os.environ.setdefault("FREEGPT4_ENABLE_GUI", "false")
os.environ.setdefault("FREEGPT4_ENABLE_HISTORY", "false")
os.environ.setdefault("FREEGPT4_REMOVE_SOURCES", "true")
os.environ.setdefault("DEFAULT_MODEL", "gpt-4")
os.environ.setdefault("DEFAULT_PROVIDER", "PollinationsAI")

try:
    from FreeGPT4_Server import app, initialize_runtime

    initialize_runtime(setup_password=False)
except Exception as exc:
    from flask import Flask, jsonify

    startup_error = f"{type(exc).__name__}: {exc}"
    app = Flask(__name__)

    @app.route("/", defaults={"path": ""}, methods=["GET", "POST"])
    @app.route("/<path:path>", methods=["GET", "POST"])
    def startup_failed(path):
        return jsonify({
            "error": "FreeGPT4 startup failed",
            "detail": startup_error,
        }), 500

application = app
