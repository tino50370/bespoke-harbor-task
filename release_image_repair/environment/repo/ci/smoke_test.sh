#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="release-api"
IMAGE_TAG="candidate"
CONTAINER_NAME="release-api-smoke-test"
HOST_PORT="18080"
CONTAINER_PORT="8080"

cleanup() {
  docker rm -f "${CONTAINER_NAME}" >/dev/null 2>&1 || true
}
trap cleanup EXIT

cleanup

echo "Starting smoke test container from ${IMAGE_NAME}:${IMAGE_TAG}"
docker run -d --name "${CONTAINER_NAME}" -p "${HOST_PORT}:${CONTAINER_PORT}" "${IMAGE_NAME}:${IMAGE_TAG}" >/dev/null

for _ in $(seq 1 20); do
  if curl -fsS "http://127.0.0.1:${HOST_PORT}/health" >/tmp/release_api_health.json 2>/dev/null; then
    break
  fi

  if ! docker ps --format '{{.Names}}' | grep -qx "${CONTAINER_NAME}"; then
    echo "Container exited before becoming healthy"
    docker logs "${CONTAINER_NAME}" || true
    exit 1
  fi

  sleep 1
done

if ! test -f /tmp/release_api_health.json; then
  echo "Health endpoint did not become available in time"
  docker logs "${CONTAINER_NAME}" || true
  exit 1
fi

grep -q '"status":"ok"' /tmp/release_api_health.json
grep -q '"service":"release-api"' /tmp/release_api_health.json

echo "Smoke test passed"