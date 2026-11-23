#!/usr/bin/env python3
"""news-image-20261122 entry: write the day's front page to /output/entry.png.

The image beside this file (entry.png) sums up the world news of Sunday
22 November 2026; this program copies it to the output directory, so
every run writes exactly the same bytes. Standard library only.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
IEND_TRAILER = b"\x00\x00\x00\x00IEND\xaeB`\x82"


def check_whole_png(path: Path) -> None:
    """Fail loudly rather than copy a truncated image: the gate only
    accepts a whole PNG (signature at the head, IEND chunk at the tail)
    of at most 1 MiB."""
    data = path.read_bytes()
    if len(data) > 1_048_576:
        raise SystemExit(f"{path.name}: {len(data)} bytes exceeds the 1 MiB cap")
    if not data.startswith(PNG_SIGNATURE) or not data.endswith(IEND_TRAILER):
        raise SystemExit(f"{path.name}: not a whole PNG")


def main() -> None:
    src = HERE / "entry.png"
    check_whole_png(src)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
