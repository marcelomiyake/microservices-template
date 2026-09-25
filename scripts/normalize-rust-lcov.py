#!/usr/bin/env python3
"""Make Rust LCOV source paths resolvable inside the Sonar scanner container."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
REPORTS = (
    ROOT / "target/coverage/example-service.lcov",
    ROOT / "target/coverage/web-api.lcov",
)


def main() -> int:
    for report in REPORTS:
        lines = report.read_text(encoding="utf-8").splitlines()
        normalized = []
        for line in lines:
            if line.startswith("SF:"):
                source = Path(line[3:]).resolve()
                try:
                    line = "SF:" + source.relative_to(ROOT).as_posix()
                except ValueError as error:
                    raise ValueError(f"LCOV source outside repository: {source}") from error
            normalized.append(line)
        report.write_text("\n".join(normalized) + "\n", encoding="utf-8")
        print(f"Normalized {report.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        raise SystemExit(2)
