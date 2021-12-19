from typing import List

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

from config import Config


class Database:

    BUCKET = "balancer"

    def __init__(self, config: Config):
        self.client = InfluxDBClient(url=config.influxdb_url, token="token", org=self.BUCKET)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def save_measure(self, record: List[Point]) -> None:
        self.write_api.write(bucket=self.BUCKET, record=record)
