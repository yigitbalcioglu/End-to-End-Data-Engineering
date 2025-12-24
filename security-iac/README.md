# Security, IAM, and IaC Module

Purpose: secure credentials, define roles, and codify infra.

## Plan
- Secrets: move DB creds to .env + Docker secrets or Vault; use Airflow Connections/Variables with backends.
- IAM: define least-privilege roles for source/destination Postgres (read vs write vs admin).
- Network: restrict ports, use SSL where possible; add ingress rules for UIs.
- Backups/DR: pg_dump/pg_restore scripts + retention policy.
- IaC: add Terraform stubs for Postgres, Airflow, and networking; parameterize with env vars.

## Quickstart
1) Create `.env` with DB creds; reference via `docker-compose.yml` secrets.
2) Add Vault dev server (optional) and enable Airflow secrets backend.
3) Create Terraform skeleton (to be added) with variables for DB users/passwords and security groups.
4) Add backup script and cron entry to run `pg_dump` to object storage or local volume.

## Next steps
- Add example `docker-compose` with secrets + Vault.
- Add Terraform templates with sample Postgres + security groups.
- Document rotation policy and RBAC mapping.
