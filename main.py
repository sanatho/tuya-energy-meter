from time import sleep

import tinytuya

from energy_meter import EnegeryMeter
from mqtt_client import MqttClient
from secret import DEVICE_ID, DEVICE_IP, LOCAL_KEY
from settings import POLL_INTERVAL

def parse_data(data):
    energy_meter = EnegeryMeter(data)
    return energy_meter

# Crea oggetto device
d = tinytuya.OutletDevice(DEVICE_ID, DEVICE_IP, LOCAL_KEY)
d.set_version(3.5)  # o 3.1, controlla tuya-cli

# Leggi stato
while True:
    data = d.status()  # restituisce dict con i datapoint locali
    energy_meter = parse_data(data['dps'])
    print(energy_meter)
    mqtt_client = MqttClient()
    mqtt_client.send(energy_meter)
    sleep(POLL_INTERVAL)
