import json
import os
from time import sleep
import subprocess

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


def get_ip_by_device_id(json_data, device_id):
    """
    Returns the IP address associated with the given device_id.
    If not found, returns None.
    :return ip None if not present
    """
    devices = json_data.get("devices", [])

    for device in devices:
        if device.get("id") == device_id:
            return device.get("ip")

    return None


def retrive_ip_address(device_id):
    subprocess.run(['python', '-m', 'tinytuya', 'scan'])

    with open('snapshot.json', 'r') as f:
        data = json.load(f)

    ip = get_ip_by_device_id(data, device_id)

    return ip


ip_adress = retrive_ip_address(DEVICE_ID)
d = tinytuya.OutletDevice(DEVICE_ID, ip_adress, LOCAL_KEY)
d.set_version(3.5)  # o 3.1, controlla tuya-cli

while True:
    data = d.status()
    energy_meter = parse_data(data['dps'])
    print(energy_meter)
    mqtt_client = MqttClient()
    mqtt_client.send(energy_meter)
    sleep(POLL_INTERVAL)
