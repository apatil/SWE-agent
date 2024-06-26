from __future__ import annotations

__version__ = "0.5.0"

from pathlib import Path
import os, sys

PACKAGE_DIR = Path(os.path.join(sys.prefix, "src/SWE-Agent/sweagent")).resolve()
assert PACKAGE_DIR.is_dir()
REPO_ROOT = PACKAGE_DIR.parent
assert REPO_ROOT.is_dir()
CONFIG_DIR = PACKAGE_DIR.parent / "config"
assert CONFIG_DIR.is_dir()


__all__ = [
    "PACKAGE_DIR",
    "CONFIG_DIR",
]
