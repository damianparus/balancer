from influxdb_client import Point

from database import Database
from meter_measure import MeterMeasureData
from real_time_power_measure import RealTimePowerMeasureData


class DataSaver:

    def __init__(self, database: Database):
        self.database = database

    def process(self, meter_measure_data: MeterMeasureData, real_time_power_measure_data: RealTimePowerMeasureData):
        point = (Point("real_time")
                 .field("real_time_grid", real_time_power_measure_data.grid)
                 .field("real_time_home", real_time_power_measure_data.home)
                 .field("real_time_pv", real_time_power_measure_data.pv)
                 .field("total_production", real_time_power_measure_data.total_production)
                 .field("meter_energy_consumed", meter_measure_data.energy_consumed)
                 .field("meter_energy_produced", meter_measure_data.energy_produced)
                 .field("meter_frequency_average", meter_measure_data.frequency_average)
                 .field("meter_voltage_ac_phase_1", meter_measure_data.voltage_ac_phase_1)
                 .field("meter_voltage_ac_phase_2", meter_measure_data.voltage_ac_phase_2)
                 .field("meter_voltage_ac_phase_3", meter_measure_data.voltage_ac_phase_3)
                 .field("meter_voltage_ac_phase_12", meter_measure_data.voltage_ac_phase_12)
                 .field("meter_voltage_ac_phase_23", meter_measure_data.voltage_ac_phase_23)
                 .field("meter_voltage_ac_phase_31", meter_measure_data.voltage_ac_phase_31)
                 .field("meter_current_ac_phase_1", meter_measure_data.current_ac_phase_1)
                 .field("meter_current_ac_phase_2", meter_measure_data.current_ac_phase_2)
                 .field("meter_current_ac_phase_3", meter_measure_data.current_ac_phase_3)
                 .field("meter_power_real_phase_1", meter_measure_data.power_real_phase_1)
                 .field("meter_power_real_phase_2", meter_measure_data.power_real_phase_2)
                 .field("meter_power_real_phase_3", meter_measure_data.power_real_phase_3)
                 .field("meter_power_real_sum", meter_measure_data.power_real_sum)
                 )
        self.database.save_measure(record=[point])
