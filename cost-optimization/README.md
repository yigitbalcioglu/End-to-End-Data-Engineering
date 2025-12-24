# Cost & Efficiency Module

Purpose: control resource usage and track spend for data infra.

## Plan
- Environment sizing: set resource limits/requests in docker-compose or Kubernetes; idle shutdown for dev services.
- Storage efficiency: prefer columnar formats (Parquet) and compression; retention policies for logs and dumps.
- Usage tracking: collect metrics (CPU/mem, Postgres disk, Kafka retention) and surface in Grafana.
- Scheduling: off-hours suspension of non-prod workloads via cron or Airflow DAG.

## Quickstart
1) Add resource limits to docker-compose services (CPU/mem) and retention configs for Kafka/Postgres backups.
2) Add Prometheus rules for quota thresholds; alert when disk/lag crosses limits.
3) Add cleanup job to prune old backups and logs.

## Next steps
- Add sample compose overrides with limits.
- Add cleanup scripts and alerts.
- Add dashboard panel for cost proxies (storage, CPU hours, message volume).
