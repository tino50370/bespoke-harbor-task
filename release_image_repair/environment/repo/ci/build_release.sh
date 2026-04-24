#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="release-api"
IMAGE_TAG="candidate"

echo "Building release image ${IMAGE_NAME}:${IMAGE_TAG}"
docker build -t "${IMAGE_NAME}:${IMAGE_TAG}" .
echo "Build completed for ${IMAGE_NAME}:${IMAGE_TAG}"