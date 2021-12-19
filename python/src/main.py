from time import sleep
from datetime import datetime

import logging

import requests as requests

from config import ConfigLoader
from database import Database
from measure import ActualMeasure

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%Y/%m/%d %H:%M:%S')

config = ConfigLoader.load()
logging.info(f"fronius_url: {config.fronius_url}")
metric_powerflow_url = f'{config.fronius_url}solar_api/v1/GetPowerFlowRealtimeData.fcgi'
metric_standard_url = f'{config.fronius_url}solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DeviceId=1&DataCollection=CommonInverterData'
metric_smartmeter_url = f'{config.fronius_url}solar_api/v1/GetMeterRealtimeData.cgi?Scope=Device&DeviceId=0'

database = Database()

while True:
    current_time = datetime.now()
    #TODO client error
    response = requests.get(metric_powerflow_url, verify=False, timeout=3)
    #TODO parse error
    response_data = response.json()
    actual_measure = ActualMeasure(
        grid=float(response_data['Body']['Data']['Site']['P_Grid']),
        pv=float(response_data['Body']['Data']['Site']['P_PV']),
        home=float(response_data['Body']['Data']['Site']['P_Load'])*-1
    )
    database.save_real_time_measure(actual_measure)
    logging.info(actual_measure)
    sleep(1)
