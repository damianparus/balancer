from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

from config import Config
from measure import RealTimePowerMeasure


class Database:

    BUCKET = "balancer"

    def __init__(self, config: Config):
        self.client = InfluxDBClient(url=config.influxdb_url, token="token", org=self.BUCKET)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def save_real_time_measure(self, measure: RealTimePowerMeasure) -> None:
        point_grid = Point("real_time").field("power", measure.grid).tag("kind", "grid")
        point_home = Point("real_time").field("power", measure.home).tag("kind", "home")
        point_pv = Point("real_time").field("power", measure.pv).tag("kind", "pv")

        self.write_api.write(bucket=self.BUCKET, record=[point_grid, point_home, point_pv])
