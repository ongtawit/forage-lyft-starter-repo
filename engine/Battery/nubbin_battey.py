from abc import ABC

from battery import Battery

from utils import add_years_to_date

class NubbinBattery(Battery, ABC):
    def __init__(self, last_service_date, current_service_date):
        self.current_date = current_service_date
        self.last_service_date = last_service_date

    def engine_should_be_serviced(self):
        engine_should_be_serviced = add_years_to_date(self.last_service_date, 2)
        if engine_should_be_serviced < self.current_date:
            return True
        return False
