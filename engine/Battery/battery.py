from abc import ABC, abstractmethod


class Battery(ABC):
    @abstractmethod
    def engine_should_be_serviced(self):
        pass