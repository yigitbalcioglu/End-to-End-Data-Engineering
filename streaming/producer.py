import json
import os
import time
from datetime import datetime
from kafka import KafkaProducer

BROKER = os.getenv("KAFKA_BROKER", "localhost:9093")
TOPIC = os.getenv("KAFKA_TOPIC", "orders")

producer = KafkaProducer(
    bootstrap_servers=[BROKER],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

print(f"Producing to {BROKER} topic={TOPIC}...")
for i in range(1, 6):
    payload = {
        "id": i,
        "user_id": i % 3 + 1,
        "status": "pending" if i % 2 else "delivered",
        "amount": float(i * 10),
        "created_at": datetime.utcnow().isoformat(),
    }
    producer.send(TOPIC, payload)
    print(f"sent {payload}")
    time.sleep(0.5)

producer.flush()
producer.close()
print("Done.")
