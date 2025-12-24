import argparse
import json
import pathlib
import requests

DEFAULT_URL = "http://localhost:8083/connectors"


def main():
    parser = argparse.ArgumentParser(description="Register Kafka Connect JDBC sink")
    parser.add_argument("--file", default="connectors/jdbc-sink.json", help="Connector JSON config")
    parser.add_argument("--url", default=DEFAULT_URL, help="Kafka Connect REST endpoint")
    args = parser.parse_args()

    config_path = pathlib.Path(args.file)
    if not config_path.exists():
        raise SystemExit(f"Config file not found: {config_path}")

    payload = json.loads(config_path.read_text())
    resp = requests.post(args.url, json=payload)
    if resp.status_code not in (200, 201):
        raise SystemExit(f"Failed: {resp.status_code} {resp.text}")
    print(f"Registered connector {payload.get('name')} at {args.url}")


if __name__ == "__main__":
    main()
