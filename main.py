"""Entrypoint that writes a specific placeholder word to the output file."""
# Entry validated: output is 1-24 chars, exactly one word, deterministic.

import os
from pathlib import Path

WORD = "placeholder"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    dir_path = Path(output_dir)
    dir_path.mkdir(parents=True, exist_ok=True)

    file_path = dir_path / "entry.txt"
    content = f"{WORD}\n"

    stripped = content.strip()
    if not (1 <= len(content) <= 24 and stripped and len(stripped.split()) == 1):
        raise ValueError("Content validation failed")

    file_path.write_text(content, encoding="utf-8")

    print(file_path)
    print(len(content))
    print(WORD)


if __name__ == "__main__":
    main()
