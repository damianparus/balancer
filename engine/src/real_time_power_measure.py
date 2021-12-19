import logging
import traceback
from dataclasses import dataclass

import requests
from influxdb_client import Point

from config import Config
from database import Database


@dataclass
class RealTimePowerMeasureData:
    grid: float
    home: float
    pv: float


class RealTimePowerMeasure:

    def __init__(self, database: Database, config: Config):
        self.metric_url = f'{config.fronius_url}solar_api/v1/GetPowerFlowRealtimeData.fcgi'
        self.database = database

    def process(self):
        try:
            response = requests.get(self.metric_url, verify=False, timeout=3)
            response_data = response.json()
            measure = RealTimePowerMeasureData(
                grid=float(response_data['Body']['Data']['Site']['P_Grid']),
                pv=float(response_data['Body']['Data']['Site']['P_PV']) if response_data['Body']['Data']['Site']['P_PV'] is not None else 0.0,
                home=float(response_data['Body']['Data']['Site']['P_Load']) * -1
            )
            record = [
                Point("real_time").field("power", measure.grid).tag("kind", "grid"),
                Point("real_time").field("power", measure.home).tag("kind", "home"),
                Point("real_time").field("power", measure.pv).tag("kind", "pv")
            ]

            self.database.save_measure(record=record)
            logging.info(measure)
        except Exception:
            logging.error("Exception: %s", traceback.format_exc())
