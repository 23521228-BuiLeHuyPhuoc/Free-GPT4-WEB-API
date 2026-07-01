import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

os.environ.setdefault("FREEGPT4_ENABLE_GUI", "false")
os.environ.setdefault("FREEGPT4_ENABLE_HISTORY", "false")
os.environ.setdefault("FREEGPT4_REMOVE_SOURCES", "true")
os.environ.setdefault("DEFAULT_MODEL", "gpt-4o")
os.environ.setdefault("DEFAULT_PROVIDER", "PollinationsAI")

from FreeGPT4_Server import app, initialize_runtime

initialize_runtime(setup_password=False)