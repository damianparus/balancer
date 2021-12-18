from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

from measure import ActualMeasure


class Database:

    BUCKET = "balancer"

    def __init__(self):
        self.client = InfluxDBClient(url="http://localhost:8086", token="token", org=self.BUCKET)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def save_real_time_measure(self, measure: ActualMeasure) -> None:
        point_grid = Point("actual_measure").field("value", measure.grid).tag("kind", "grid")
        point_home = Point("actual_measure").field("value", measure.home).tag("kind", "home")
        point_pv = Point("actual_measure").field("value", measure.pv).tag("kind", "pv")

        self.write_api.write(bucket=self.BUCKET, record=[point_grid, point_home, point_pv])
