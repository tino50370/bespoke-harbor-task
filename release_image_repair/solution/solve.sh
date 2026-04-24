#!/usr/bin/env bash
set -euo pipefail

cd /app/repo

cat > service/requirements.txt <<'EOF'
fastapi==0.115.0
uvicorn==0.30.6
EOF