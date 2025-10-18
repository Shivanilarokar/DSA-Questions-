from fastapi import FastAPI, Request
import logging, sys, json, os

# ---------------- Logger Setup ----------------
def setup_logger():
    """Sets up simple Azure/console friendly logging."""
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
