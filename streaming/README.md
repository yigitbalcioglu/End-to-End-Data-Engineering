# Streaming Module (Kafka → Postgres)

Purpose: cover real-time ingest alongside batch ELT.

## Plan
- Spin up Kafka + ZooKeeper + Kafka Connect via Docker Compose; use Python producer and JDBC sink connector to Postgres.
- Define a sample `orders` topic schema; optional schema registry with Confluent or Redpanda.
- Build a small consumer/ingestion service to upsert into Postgres with idempotency.
- Add monitoring for consumer lag.

## Quickstart
1) `docker-compose up` for kafka, zookeeper, kafka-connect, postgres.
2) Install deps and send sample data: `pip install -r requirements.txt && python producer.py`.
3) Create sink connector (choose one):
	- Linux/macOS: `curl -X POST -H "Content-Type: application/json" --data @connectors/jdbc-sink.json http://localhost:8083/connectors`
	- Windows/Python: `python register_connector.py`
4) Verify rows in Postgres `orders_sink` table on port 5440 (user/pass `postgres`).
5) Optional: run custom consumer (idempotent upsert) `python consumer.py`.

## Next steps
- Add docker-compose and sample producer/consumer scripts.
- Add schema registry and basic Avro/JSON schema validation.
- Integrate with Airflow DAG to run stream checks or micro-batch merges.
