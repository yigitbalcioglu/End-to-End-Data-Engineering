# Data Quality Module

Purpose: add data quality checks to ELT (dbt tests + Great Expectations) for the existing Postgres source/destination.

## Plan
- Set up Python venv and install `dbt-postgres` and `great_expectations`.
- Add dbt tests: uniqueness/not_null/schema.yml under `models/` pointing to destination Postgres from docker-compose.
- Add Great Expectations suite: connect to destination Postgres via SQLAlchemy URI, create expectations for row counts, domain values, and freshness.
- Wire into pipeline: run dbt tests after Airbyte sync; run GE checkpoint via Airflow task; fail DAG on quality failure.

## Quickstart
1) `python -m venv .venv && .venv/Scripts/activate`
2) `pip install dbt-postgres great_expectations`
3) Copy `profiles.yml` pointing to destination Postgres (port 5434) and run `dbt test`.
4) `great_expectations init` and create a datasource for Postgres; add an expectation suite and checkpoint.
5) Add an Airflow task (or GitHub Actions) to call `dbt test` + `ge checkpoint run`.

## Next steps
- Add sample `schema.yml` and one GE expectation suite.
- Add CI job to block merges on failing tests.
