from __future__ import annotations

from pathlib import Path


class Paths():
   ROOT = Path( __file__ ).resolve().parent.parent
   INPUT_DIR = ROOT / 'input'
   OUTPUT_DIR = ROOT / 'output'
