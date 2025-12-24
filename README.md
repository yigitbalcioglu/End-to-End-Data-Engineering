# Data Engineering Playground

Bu depo çoklu alt projeler içerir; her klasör belirli bir beceriyi/pratiği gösterir.

## Klasörler ve Amaçları
- **custom-elt-project-main**: Docker Compose ile kaynak/dest Postgres ve Python ELT scripti; temel batch ELT örneği.
- **custom-elt-project-airbyte**: Airbyte + Airflow + dbt ile modern ELT orkestrasyonu; UI üzerinden kaynak/hedef kurup DAG ile tetiklenir.
- **custom-elt-project-airflow**: Airflow DAG’ı ile zamanlanmış ELT; CRON tabanlı çalıştırma.
- **custom-elt-project-dbt**: dbt merkezli dönüşümler; dbt projeleri ve örnek modeller.
- **custom-elt-project-airflow**: Airflow ile temel DAG orchestration (üstte belirtildi).
- **custom-elt-project-main/elt_script**: ELT Python scripti ve Dockerfile’ı.
- **data-quality**: dbt testleri ve Great Expectations ile veri kalitesi kontrolleri; `run_checks.sh` ile dbt test + GE checkpoint.
- **governance-lineage**: OpenMetadata hızlı başlatma, Airflow/OpenLineage ve Postgres ingestion config’leri.
- **security-iac**: .env örneği, Postgres yedekleme scripti, Terraform başlangıç dosyası; gizli yönetimi ve altyapı temeli.
- **streaming**: Kafka/ZooKeeper + Kafka Connect + Postgres; Python producer/consumer, JDBC sink connector örneği.
- **observability-monitoring**: Prometheus + Grafana + exporter’lar; otomatik Prometheus datasource provision’ı.
- **cost-optimization**: Docker Compose override ile kaynak limitleri ve temizlik scriptleri.
- **customer-satisfaction-mlops-main**: ZenML + MLflow ile MLOps uçtan uca örnek, Streamlit uygulaması.
- **data-quality (dbt/gx)**: dbt ve Great Expectations yapılandırmaları.
- **governance-lineage/ingestion**: OpenMetadata ingest YAML’ları.
- **security-iac/scripts**: pg_dump yedekleme; **security-iac/terraform**: Terraform şablonu.

## Hızlı Başlangıç Önerisi
1) Batch ELT: `custom-elt-project-main` dizininde `docker-compose up` ve süreci izle.
2) Modern ELT: `custom-elt-project-airbyte` / `custom-elt-project-airflow` ile Airbyte+Airflow+dbt hattını çalıştır.
3) Kalite: `data-quality` klasöründe env ayarla ve `./run_checks.sh` çalıştır.
4) Streaming: `streaming` klasöründe `docker-compose up`, ardından `python producer.py` ve `python register_connector.py`.
5) Gözlemlenebilirlik: `observability-monitoring` klasöründe stack’i aç, Grafana (admin/admin) ile metrikleri izle.
6) Yönetişim/Lineage: `governance-lineage` compose’u aç, ingestion YAML’ları ile metadata gönder.
