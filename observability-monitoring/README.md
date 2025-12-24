# Observability & Monitoring Module

Purpose: add metrics, logs, and alerts for pipelines and infra.

## Plan
- Metrics: Prometheus scraping Airflow, Kafka, Postgres exporters; custom app metrics via pushgateway.
- Logs: Loki (or ELK) stack; ship container logs with Promtail/Fluent Bit.
- Dashboards: Grafana boards for DAG success rate, task duration, db CPU/IO, Kafka lag.
- Alerts: Grafana Alerting or Alertmanager rules (email/Slack/webhook).

## Quickstart
1) `docker-compose up` (to be added) with Prometheus + Grafana + exporters + Loki.
2) Point exporters: `postgres_exporter` to both DBs, `kafka_exporter` to Kafka.
3) Add Airflow statsd/exporter and wire to Prometheus.
4) Create Grafana dashboard (JSON model) and sample alerts.

## Next steps
- Add compose file and Prometheus config.
- Add sample Grafana dashboards and alert rules.
- Add log shipper config (Promtail) for containers.
