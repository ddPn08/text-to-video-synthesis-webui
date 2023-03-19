import importlib
import argparse
import os
import sys


def is_webui_extension():
    try:
        importlib.import_module("webui")
        return True
    except:
        return False


ROOT_DIR = (
    importlib.import_module("modules.scripts").basedir()
    if is_webui_extension()
    else os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
)

parser = argparse.ArgumentParser()
parser.add_argument("--share", action="store_true")
parser.add_argument("--port", type=int, default=None)
parser.add_argument("--host", type=str, default=None)
parser.add_argument("--ngrok", type=str, default=None)
parser.add_argument("--ngrok-region", type=str, default="us")
cmd_opts, _ = parser.parse_known_args(sys.argv)
