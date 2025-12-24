import json
import os
import psycopg2
from kafka import KafkaConsumer

BROKER = os.getenv("KAFKA_BROKER", "localhost:9093")
TOPIC = os.getenv("KAFKA_TOPIC", "orders")

PG_CONN = {
    "host": os.getenv("PG_HOST", "localhost"),
    "port": int(os.getenv("PG_PORT", "5440")),
    "user": os.getenv("PG_USER", "postgres"),
    "password": os.getenv("PG_PASSWORD", "postgres"),
    "dbname": os.getenv("PG_DB", "streaming"),
}

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=[BROKER],
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    enable_auto_commit=True,
    auto_offset_reset="earliest",
)

conn = psycopg2.connect(**PG_CONN)
conn.autocommit = True
cur = conn.cursor()
cur.execute(
    """
    create table if not exists orders_stream (
      id bigint primary key,
      user_id bigint,
      status text,
      amount numeric,
      created_at timestamptz
    );
    """
)

print(f"Consuming from {BROKER} topic={TOPIC} -> postgres {PG_CONN['host']}:{PG_CONN['port']}")
for msg in consumer:
    record = msg.value
    cur.execute(
        """
        insert into orders_stream (id, user_id, status, amount, created_at)
        values (%s, %s, %s, %s, %s)
        on conflict (id) do update set
          user_id = excluded.user_id,
          status = excluded.status,
          amount = excluded.amount,
          created_at = excluded.created_at;
        """,
        (
          record.get("id"),
          record.get("user_id"),
          record.get("status"),
          record.get("amount"),
          record.get("created_at"),
        ),
    )
    print(f"upserted {record}")
