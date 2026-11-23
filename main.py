"""Write the make.fun bounty entry text to entry.txt.

Standard library only, no network. The text is one string constant and is
written as UTF-8 bytes with no trailing newline.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "The cat has not moved since six.\n"
    "The square of light has, and takes her with it."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get(
        "OUTPUT_DIR", "/output"
    )
    out_dir = Path(folder)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
