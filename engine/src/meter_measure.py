import logging
import requests

from config import Config
from dataclasses import dataclass


@dataclass
class MeterMeasureData:
    energy_consumed: float
    energy_produced: float
    frequency_average: float
    voltage_ac_phase_1: float
    voltage_ac_phase_2: float
    voltage_ac_phase_3: float
    voltage_ac_phase_12: float
    voltage_ac_phase_23: float
    voltage_ac_phase_31: float
    current_ac_phase_1: float
    current_ac_phase_2: float
    current_ac_phase_3: float
    power_real_phase_1: float
    power_real_phase_2: float
    power_real_phase_3: float
    power_real_sum: float


class MeterMeasure:

    def __init__(self, config: Config):
        self.metric_url = f'{config.fronius_url}solar_api/v1/GetMeterRealtimeData.cgi?Scope=Device&DeviceId=0'

    def get(self) -> MeterMeasureData:
        response = requests.get(self.metric_url, verify=False, timeout=3)
        response_data = response.json()
        measure = MeterMeasureData(
            energy_consumed=float(response_data['Body']['Data']['EnergyReal_WAC_Sum_Consumed']),
            energy_produced=float(response_data['Body']['Data']['EnergyReal_WAC_Sum_Produced']),
            frequency_average=float(response_data['Body']['Data']['Frequency_Phase_Average']),
            voltage_ac_phase_1=float(response_data['Body']['Data']['Voltage_AC_Phase_1']),
            voltage_ac_phase_2=float(response_data['Body']['Data']['Voltage_AC_Phase_2']),
            voltage_ac_phase_3=float(response_data['Body']['Data']['Voltage_AC_Phase_3']),
            voltage_ac_phase_12=float(response_data['Body']['Data']['Voltage_AC_PhaseToPhase_12']),
            voltage_ac_phase_23=float(response_data['Body']['Data']['Voltage_AC_PhaseToPhase_23']),
            voltage_ac_phase_31=float(response_data['Body']['Data']['Voltage_AC_PhaseToPhase_31']),
            current_ac_phase_1=float(response_data['Body']['Data']['Current_AC_Phase_1']),
            current_ac_phase_2=float(response_data['Body']['Data']['Current_AC_Phase_2']),
            current_ac_phase_3=float(response_data['Body']['Data']['Current_AC_Phase_3']),
            power_real_phase_1=float(response_data['Body']['Data']['PowerReal_P_Phase_1']),
            power_real_phase_2=float(response_data['Body']['Data']['PowerReal_P_Phase_2']),
            power_real_phase_3=float(response_data['Body']['Data']['PowerReal_P_Phase_3']),
            power_real_sum=float(response_data['Body']['Data']['PowerReal_P_Sum'])
        )
        logging.info(measure)

        return measure
