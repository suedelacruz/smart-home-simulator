class EnergyService:

    def __init__(self, strategy):

        self._strategy = strategy

    def calculate_total_energy(
        self,
        devices
    ):

        return self._strategy.calculate(
            devices
        )