# Release API

This repository contains the service used by the release pipeline smoke checks.


## Local development

Run locally:

```bash
uvicorn app:app --host 0.0.0.0 --port 8080
```

## Health checks

The service exposes a health endpoint used by internal checks.

## CI notes

The CI workflow builds a release image and validates the service with a smoke test.