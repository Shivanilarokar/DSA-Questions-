from fastapi import FastAPI, Request
import logging, sys, json

# ---------------- Logging setup ----------------
def setup_logger():
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
    )
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)
    return logging.getLogger("main")

logger = setup_logger()

# ---------------- FastAPI app ----------------
app = FastAPI()

# ---------------- Helper functions ----------------
def extract_commit_info(commit: dict) -> dict:
    """Extracts useful information from a single commit."""
    return {
        "commit_id": commit.get("id", "")[:7],
        "message": commit.get("message", ""),
        "author": commit.get("author", {}).get("name", "unknown"),
        "added": commit.get("added", []),
        "modified": commit.g
