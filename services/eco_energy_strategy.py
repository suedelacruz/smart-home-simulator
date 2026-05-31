from services.energy_stategy import EnergyStrategy


class EcoEnergyStrategy(EnergyStrategy):

    def calculate(self, devices):

        total = 0

        for device in devices:
            total += device.energy_consumption

        return total * 0.8