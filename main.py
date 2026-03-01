from time import sleep

import tinytuya

from energy_meter import EnegeryMeter
from mqtt_client import MqttClient
from secret import DEVICE_ID, DEVICE_IP, LOCAL_KEY
from settings import POLL_INTERVAL

def parse_data(data):
    """
    Parse raw data from tinytuya
    :param data: Raw data from tinytuya
    :return: Energy meter object
    """
    
    energy_meter = EnegeryMeter(data)
    return energy_meter

d = tinytuya.OutletDevice(DEVICE_ID, DEVICE_IP, LOCAL_KEY)
d.set_version(3.5)  # o 3.1, controlla tuya-cli

while True:
    data = d.status()
    energy_meter = parse_data(data['dps'])
    print(energy_meter)
    mqtt_client = MqttClient()
    mqtt_client.send(energy_meter)
    sleep(POLL_INTERVAL)
