#!/usr/bin/env bash
set -euo pipefail

# Activate venv if present
if [[ -d .venv ]]; then
  source .venv/Scripts/activate 2>/dev/null || source .venv/bin/activate
fi

export DBT_PROFILES_DIR=${DBT_PROFILES_DIR:-$(pwd)}

echo "Running dbt tests..."
dbt test --select stg_orders

echo "Running Great Expectations checkpoint..."
great_expectations --v3-api checkpoint run orders_checkpoint

echo "Done."
