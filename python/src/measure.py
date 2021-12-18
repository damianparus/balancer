from dataclasses import dataclass


@dataclass
class ActualMeasure:
    grid: float
    home: float
    pv: float
