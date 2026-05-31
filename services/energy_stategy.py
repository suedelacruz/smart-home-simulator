from abc import ABC, abstractmethod


class EnergyStrategy(ABC):

    @abstractmethod
    def calculate(self, devices):
        pass