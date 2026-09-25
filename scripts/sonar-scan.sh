#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
: "${SONAR_TOKEN:?Set SONAR_TOKEN in the environment before scanning.}"
export SONAR_HOST_URL="${SONAR_HOST_URL:-http://127.0.0.1:9000}"
scanner_image="${SONAR_SCANNER_IMAGE:-sonarsource/sonar-scanner-cli:latest}"

command -v docker >/dev/null || { echo 'Docker is required for the scanner image.' >&2; exit 2; }
"$root_dir/scripts/coverage.sh"
mkdir -p "$root_dir/target/coverage"
(
  cd "$root_dir"
  cargo clippy -p example-service --all-targets --locked --message-format=json -- -D warnings > target/coverage/example-service-clippy.json
  cargo clippy -p web-api --all-targets --locked --message-format=json -- -D warnings > target/coverage/web-api-clippy.json
)

for project in example-service web-api web; do
  docker run --rm --network host \
    --volume "$root_dir:/usr/src" \
    --env SONAR_HOST_URL --env SONAR_TOKEN \
    --workdir /usr/src \
    "$scanner_image" \
    "-Dproject.settings=.sonar/$project.properties" \
    "-Dsonar.working.directory=/usr/src/target/sonar-$project" \
    -Dsonar.qualitygate.wait=true
done

python3 "$root_dir/scripts/check-sonar-gate.py"
