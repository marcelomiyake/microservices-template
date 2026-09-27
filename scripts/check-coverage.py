#!/usr/bin/env python3
"""Check the three local LCOV reports against the PoC line coverage target."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
REPORTS = {
    "example-service library": ROOT / "target/coverage/example-service.lcov",
    "web-api library": ROOT / "target/coverage/web-api.lcov",
    "Vue frontend": ROOT / "web/coverage/lcov.info",
}
MINIMUM = 80.0


def line_coverage(path: Path) -> tuple[int, int]:
    covered = total = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("LF:"):
            total += int(line[3:])
        elif line.startswith("LH:"):
            covered += int(line[3:])
    if total == 0:
        raise ValueError(f"{path} contains no coverable lines")
    return covered, total


def main() -> int:
    failed = False
    for name, path in REPORTS.items():
        if not path.is_file():
            print(f"MISSING {name}: {path}", file=sys.stderr)
            failed = True
            continue
        covered, total = line_coverage(path)
        percent = 100 * covered / total
        result = "PASS" if percent >= MINIMUM else "FAIL"
        print(f"{result} {name}: {percent:.1f}% ({covered}/{total} lines)")
        failed |= percent < MINIMUM
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        raise SystemExit(2)
