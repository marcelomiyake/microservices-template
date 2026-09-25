#!/usr/bin/env python3
"""Require a server gate and overall coverage, duplication, and issue checks."""

import base64
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

PROJECTS = (
    "microservices-template-example-service",
    "microservices-template-web-api",
    "microservices-template-web",
)


def read_api(path: str) -> dict:
    host = os.environ.get("SONAR_HOST_URL", "http://127.0.0.1:9000").rstrip("/")
    token = os.environ["SONAR_TOKEN"]
    request = Request(f"{host}{path}")
    request.add_header(
        "Authorization", "Basic " + base64.b64encode(f"{token}:".encode()).decode()
    )
    with urlopen(request, timeout=20) as response:
        return json.load(response)


def main() -> int:
    failed = False
    for project in PROJECTS:
        gate = read_api(
            "/api/qualitygates/project_status?" + urlencode({"projectKey": project})
        )["projectStatus"]
        measures = read_api(
            "/api/measures/component?"
            + urlencode(
                {
                    "component": project,
                    "metricKeys": "coverage,duplicated_lines_density,security_hotspots",
                }
            )
        )["component"]["measures"]
        values = {item["metric"]: float(item["value"]) for item in measures}
        coverage = values.get("coverage")
        duplication = values.get("duplicated_lines_density")
        hotspots = values.get("security_hotspots")
        issues = read_api(
            "/api/issues/search?"
            + urlencode({"componentKeys": project, "resolved": "false", "ps": 1})
        )["total"]
        okay = (
            gate["status"] == "OK"
            and coverage is not None
            and coverage >= 80
            and duplication is not None
            and duplication < 3
            and hotspots == 0
            and issues == 0
        )
        label = "PASS" if okay else "FAIL"
        print(
            f"{label} {project}: server gate={gate['status']}, "
            f"coverage={coverage}, duplication={duplication}, "
            f"security hotspots={hotspots}, active issues={issues}"
        )
        failed |= not okay
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (HTTPError, URLError, KeyError, ValueError, OSError) as error:
        print(f"SonarQube gate unavailable: {error}", file=sys.stderr)
        raise SystemExit(2)
