# Governance & Lineage Module

Purpose: add discovery, catalog, and lineage for datasets and pipelines.

## Plan
- Choose lightweight catalog: OpenMetadata (default) or DataHub; run via Docker Compose.
- Register source and destination Postgres, Airbyte connection, dbt models, and Airflow DAGs to emit lineage.
- Enable dbt OpenLineage or datahub-openlineage plugin to publish run metadata.
- Add ownership, tags, PII classifications, and glossary terms.

## Quickstart
1) Spin up OpenMetadata quickstart (see docker-compose.yml to be added).
2) Install emitter: `pip install openlineage-airflow` (Airflow) and `pip install datahub` if you choose DataHub.
3) Configure Airflow lineage backend to point to the OpenLineage endpoint.
4) Run a DAG; verify lineage graph for source→Airbyte→dbt→destination.

## Next steps
- Add docker-compose for OpenMetadata/DataHub.
- Add sample lineage config in Airflow DAG and dbt `profiles.yml`.
- Add data classifications and owners for key tables.
