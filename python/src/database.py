from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

from measure import ActualMeasure


class Database:

    BUCKET = "balancer"

    def __init__(self):
        self.client = InfluxDBClient(url="http://localhost:8086", token="token", org=self.BUCKET)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def save_real_time_measure(self, measure: ActualMeasure) -> None:
        point = (Point("actual_measure")
                 .field("grid", measure.grid)
                 .field("home", measure.home)
                 .field("pv", measure.pv))

        self.write_api.write(bucket=self.BUCKET, record=point)

        query_api = self.client.query_api()
        tables = query_api.query('from(bucket:"balancer") |> range(start: -10m)')
        for table in tables:
            print(table)
            for row in table.records:
                print(row.values)
