import json
import paho.mqtt.publish as publish

BROKER = "192.168.1.100"

def publish_config(topic, payload):
    publish.single(topic, json.dumps(payload), hostname=BROKER, retain=True)

device = {
    "identifiers": ["pinza_1"],
    "name": "Pinza Energia",
    "manufacturer": "Tuya",
    "model": "Clamp Meter"
}

configs = [
    ("homeassistant/sensor/pinza_voltage/config", {
        "name": "Tensione",
        "state_topic": "casa/pinza/voltage",
        "unit_of_measurement": "V",
        "device_class": "voltage",
        "unique_id": "pinza_voltage_1",
        "device": device
    }),
    ("homeassistant/sensor/pinza_current/config", {
        "name": "Corrente",
        "state_topic": "casa/pinza/current",
        "unit_of_measurement": "A",
        "device_class": "current",
        "unique_id": "pinza_current_1",
        "device": device
    }),
    ("homeassistant/sensor/pinza_power/config", {
        "name": "Potenza",
        "state_topic": "casa/pinza/power",
        "unit_of_measurement": "W",
        "device_class": "power",
        "unique_id": "pinza_power_1",
        "device": device
    }),
    ("homeassistant/sensor/pinza_energy/config", {
        "name": "Energia",
        "state_topic": "casa/pinza/energy",
        "unit_of_measurement": "kWh",
        "device_class": "energy",
        "state_class": "total_increasing",
        "unique_id": "pinza_energy_1",
        "device": device
    }),
]

for topic, payload in configs:
    publish_config(topic, payload)