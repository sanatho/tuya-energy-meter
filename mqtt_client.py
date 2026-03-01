import json

import paho.mqtt.client as mqtt
from settings import MQTT_KEEP_ALIVE, MQTT_BROKER, MQTT_PORT, MQTT_TOPIC_CURRENT, MQTT_TOPIC_POWER, MQTT_TOPIC_VOLTAGE, MQTT_TOPIC_COMPLETE


class MqttClient:
    def __init__(self):
        """
        Constructor for mqtt client
        """
        
        self.port = MQTT_PORT
        self.address = MQTT_BROKER
        self.keep_alive = MQTT_KEEP_ALIVE

        mqtt_client = mqtt.Client()
        mqtt_client.connect(self.address, self.port, self.keep_alive)
        mqtt_client.loop_start()

        self.client = mqtt_client
    
    def send(self, energy_meter):
        """
        Send data for auto-discovery in home-assistant
        :param energy_meter: Energy meter object
        """

        device_info = {
            "identifiers": ["energy_meter_1"],
            "name": "Energy Meter",
            "manufacturer": "Tuya",
            "model": "Clamp Meter",
            "configuration_url": "https://github.com/sanatho/tuya-energy-meter"
        }

        configs = [
            {
                "topic": "homeassistant/sensor/energy_meter_voltage/config",
                "payload": {
                    "name": "Tensione",
                    "state_topic": "home/energy_meter/voltage",
                    "unit_of_measurement": "V",
                    "device_class": "voltage",
                    "unique_id": "energy_meter_voltage_1",
                    "device": device_info
                }
            },
            {
                "topic": "homeassistant/sensor/energy_meter_current/config",
                "payload": {
                    "name": "Corrente",
                    "state_topic": "home/energy_meter/current",
                    "unit_of_measurement": "A",
                    "device_class": "current",
                    "unique_id": "energy_meter_current_1",
                    "device": device_info
                }
            },
            {
                "topic": "homeassistant/sensor/energy_meter_power/config",
                "payload": {
                    "name": "Potenza",
                    "state_topic": "home/energy_meter/power",
                    "unit_of_measurement": "W",
                    "device_class": "power",
                    "unique_id": "energy_meter_power_1",
                    "device": device_info
                }
            }
        ]

        for cfg in configs:
            self.client.publish(cfg["topic"], json.dumps(cfg["payload"]), retain=True)

        self.client.publish("home/energy_meter/voltage", str(energy_meter.voltage))
        self.client.publish("home/energy_meter/current", str(energy_meter.current))
        self.client.publish("home/energy_meter/power", str(energy_meter.power))