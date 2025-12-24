#!/usr/bin/env bash
set -euo pipefail

# Delete local Docker images/volumes older than N days; default 14.
DAYS=${1:-14}

echo "Pruning dangling images and volumes older than $DAYS days..."
docker image prune -af --filter "until=${DAYS}d"
docker volume prune -f --filter "until=${DAYS}d"

echo "Done."
