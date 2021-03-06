from dataclasses import dataclass
import argparse


@dataclass
class Config:
    fronius_url: str
    influxdb_url: str


class ConfigLoader:

    @staticmethod
    def load() -> Config:
        parser = argparse.ArgumentParser()
        parser.add_argument('--fronius-url', default=None, required=True, type=str)
        parser.add_argument('--influxdb-url', default=None, required=True, type=str)
        args, argv = parser.parse_known_args()

        return Config(
            fronius_url=args.fronius_url,
            influxdb_url=args.influxdb_url
        )
