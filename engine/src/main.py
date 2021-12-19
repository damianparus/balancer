import logging
from time import sleep

from config import ConfigLoader
from database import Database
from real_time_power_measure import RealTimePowerMeasure

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%Y/%m/%d %H:%M:%S')

config = ConfigLoader.load()
logging.info(f"fronius_url: {config.fronius_url}")
logging.info(f"influxdb_url: {config.influxdb_url}")

metric_standard_url = f'{config.fronius_url}solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DeviceId=1&DataCollection=CommonInverterData'
metric_smartmeter_url = f'{config.fronius_url}solar_api/v1/GetMeterRealtimeData.cgi?Scope=Device&DeviceId=0'

database = Database(config)
real_time_power_measure = RealTimePowerMeasure(database=database, config=config)

while True:
    real_time_power_measure.process()
    sleep(5)
