import logging
import traceback
from time import sleep

from config import ConfigLoader
from data_saver import DataSaver
from database import Database
from meter_measure import MeterMeasure
from real_time_power_measure import RealTimePowerMeasure

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, datefmt='%Y/%m/%d %H:%M:%S')

config = ConfigLoader.load()
logging.info(f"fronius_url: {config.fronius_url}")
logging.info(f"influxdb_url: {config.influxdb_url}")

#metric_standard_url = f'{config.fronius_url}solar_api/v1/GetInverterRealtimeData.cgi?Scope=Device&DeviceId=1&DataCollection=CommonInverterData'

database = Database(config)
real_time_power_measure = RealTimePowerMeasure(config=config)
meter_measure = MeterMeasure(config=config)
data_saver = DataSaver(database=database)

while True:
    # TODO switch to async
    try:
        real_time_power_measure_data = real_time_power_measure.get()
        meter_measure_data = meter_measure.get()
        data_saver.process(meter_measure_data=meter_measure_data, real_time_power_measure_data=real_time_power_measure_data)
    except Exception:
        logging.error("Exception: %s", traceback.format_exc())
    sleep(5)
