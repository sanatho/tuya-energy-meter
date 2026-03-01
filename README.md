# Tuya Energy Meter

A small Python project to read energy data from Tuya-compatible devices and publish readings via MQTT.

**Quick summary**
- Reads energy data from Tuya devices using the local Python SDK
- Publishes measurements to an MQTT broker
- Supports running locally or via Docker / docker-compose

**Repository layout**
- `main.py` — app entry point
- `energy_meter.py` — device polling and parsing logic
- `mqtt_client.py` — MQTT connection and publish helpers
- `settings.py` — configurable settings (MQTT, intervals, topics)
- `secret.py` — device credentials and secrets (keep private)
- `requirements.txt` — Python dependencies
- `Dockerfile`, `docker-compose.yml` — containerized run

## Requirements
- Python 3.14+
- A running MQTT broker (local or remote)

## Installation (local)

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration
- Copy or edit `secret.py` to include your Tuya device credentials and keys. This file is intentionally kept out of version control — never commit secrets.
- Update `settings.py` to point to your MQTT broker, topics, and polling intervals.

## Running

Run the application directly:

```bash
source .venv/bin/activate
python main.py
```

This will start polling your Tuya energy device(s) and publish readings to the configured MQTT topics.

## Docker

Build and run with docker-compose:

```bash
docker compose build
docker compose up
```

Or build the image with the included `Dockerfile` and run it pointing to your environment/config.

## Notes & Security
- Keep `secret.py` out of source control. Use environment variables or Docker secrets when deploying.
- The project includes a local virtual environment under `bin/` and `lib/` — you may want to exclude those folders from commits or recreate a clean venv in other environments.

## Contributing
- Feel free to open issues or PRs for bug fixes and improvements.

## To-Do
- Add autodiscovery for Tuya energy meter IP address (discover device on local network and populate `TUYA_DEVICE_IP` in `secret.py`)
