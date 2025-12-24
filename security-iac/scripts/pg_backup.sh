#!/usr/bin/env bash
set -euo pipefail

# Usage: ./pg_backup.sh source|dest backup.sql
ROLE=${1:-dest}
OUT=${2:-backup.sql}

if [[ "$ROLE" == "source" ]]; then
  HOST=${SOURCE_POSTGRES_HOST:-localhost}
  PORT=${SOURCE_POSTGRES_PORT:-5433}
  USER=${SOURCE_POSTGRES_USER:-postgres}
  DB=${SOURCE_POSTGRES_DB:-postgres}
  PASS=${SOURCE_POSTGRES_PASSWORD:-postgres}
else
  HOST=${DEST_POSTGRES_HOST:-localhost}
  PORT=${DEST_POSTGRES_PORT:-5434}
  USER=${DEST_POSTGRES_USER:-postgres}
  DB=${DEST_POSTGRES_DB:-postgres}
  PASS=${DEST_POSTGRES_PASSWORD:-postgres}
fi

export PGPASSWORD="$PASS"
pg_dump -h "$HOST" -p "$PORT" -U "$USER" -d "$DB" -Fc -f "$OUT"
echo "Backup written to $OUT"
