import logging
import requests

from config import Config
from dataclasses import dataclass


@dataclass
class RealTimePowerMeasureData:
    grid: float
    home: float
    pv: float
    total_production: float


class RealTimePowerMeasure:

    def __init__(self, config: Config):
        self.metric_url = f'{config.fronius_url}solar_api/v1/GetPowerFlowRealtimeData.fcgi'

    def get(self) -> RealTimePowerMeasureData:
        response = requests.get(self.metric_url, verify=False, timeout=3)
        response_data = response.json()
        measure = RealTimePowerMeasureData(
            grid=float(response_data['Body']['Data']['Site']['P_Grid']),
            pv=float(response_data['Body']['Data']['Site']['P_PV']) if response_data['Body']['Data']['Site']['P_PV'] is not None else 0.0,
            home=float(response_data['Body']['Data']['Site']['P_Load']) * -1,
            total_production=float(response_data['Body']['Data']['Site']["E_Total"])
        )
        logging.info(measure)
        return measure