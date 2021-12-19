from dataclasses import dataclass


@dataclass
class RealTimePowerMeasure:
    grid: float
    home: float
    pv: float
