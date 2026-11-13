"""Entry for make.fun competition ai-happy-01.

Copies the entry image to the output directory (honouring
MAKEFUN_OUTPUT_DIR, default /output). Deterministic: every run writes
the same bytes.
"""

import os
import shutil


# The image is JPEG bytes stored as image.png; the gate reads the file
# by its first bytes, so the name stays entry.png either way.
def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copyfile(
        os.path.join(here, "image.png"),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
