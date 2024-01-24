import unittest
from datetime import date
from engine.Battery.nubbin_battey import NubbinBattery
from engine.Battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2016-01-25")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.engine_should_be_serviced())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.engine_should_be_serviced())


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2018-01-25")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.engine_should_be_serviced())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.engine_should_be_serviced())

    class TestCapuletEngine(unittest.TestCase):
        def test_needs_service_true(self):
            current_mileage = 30001
            last_service_mileage = 0
            engine = CapuletEngine(current_mileage, last_service_mileage)
            self.assertTrue(engine.needs_service())

        def test_needs_service_false(self):
            current_mileage = 30000
            last_service_mileage = 0
            engine = CapuletEngine(current_mileage, last_service_mileage)
            self.assertFalse(engine.needs_service())

    class TestSternmanEngine(unittest.TestCase):
        def test_needs_service_true(self):
            warning_light_is_on = True
            engine = SternmanEngine(warning_light_is_on)
            self.assertTrue(engine.needs_service())

        def test_needs_service_false(self):
            warning_light_is_on = False
            engine = SternmanEngine(warning_light_is_on)
            self.assertFalse(engine.needs_service())

    class TestWilloughbyEngine(unittest.TestCase):
        def test_needs_service_true(self):
            current_mileage = 60001
            last_service_mileage = 0
            engine = WilloughbyEngine(current_mileage, last_service_mileage)
            self.assertTrue(engine.needs_service())

        def test_needs_service_false(self):
            current_mileage = 60000
            last_service_mileage = 0
            engine = WilloughbyEngine(current_mileage, last_service_mileage)
            self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
