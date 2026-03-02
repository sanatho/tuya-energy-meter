import json
from time import sleep, time
import subprocess

import tinytuya

from energy_meter import EnegeryMeter
from mqtt_client import MqttClient
from secret import DEVICE_ID, LOCAL_KEY
from settings import AUTODISCOVERY_INTERVALS, POLL_INTERVAL

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


ip_address = retrive_ip_address(DEVICE_ID)
d = tinytuya.OutletDevice(DEVICE_ID, ip_address, LOCAL_KEY)
d.set_version(3.5)  # o 3.1, controlla tuya-cli
mqtt_client = MqttClient()
last_run = 0

while True:
    now = time()
    data = d.status()
    energy_meter = parse_data(data['dps'])
    mqtt_client.send(energy_meter)

    # run the extra function every 30 minutes
    if now - last_run >= AUTODISCOVERY_INTERVALS * 60:
        ip_address = retrive_ip_address(DEVICE_ID)
        d = tinytuya.OutletDevice(DEVICE_ID, ip_address, LOCAL_KEY)
        last_run = now  # reset timer

    print(energy_meter)
    sleep(POLL_INTERVAL)
