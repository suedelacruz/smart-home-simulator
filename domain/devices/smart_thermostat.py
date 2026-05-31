from domain.devices.smart_device import SmartDevice


class SmartThermostat(SmartDevice):

    def __init__(
        self,
        device_id,
        name,
        room,
        target_temperature=22,
        current_temperature=22,
        eco_mode=False
    ):

        super().__init__(device_id, name, room)

        self._target_temperature = target_temperature
        self._current_temperature = current_temperature
        self._eco_mode = eco_mode

    def set_target_temperature(self, temperature):
        self._target_temperature = temperature

    def toggle_eco_mode(self):
        self._eco_mode = not self._eco_mode

    def get_status(self):

        return (
            f"{self.name} | "
            f"Power: {'ON' if self.power_state else 'OFF'} | "
            f"Current Temp: {self._current_temperature}°C | "
            f"Target Temp: {self._target_temperature}°C | "
            f"Eco Mode: {self._eco_mode}"
        )
    