from domain.devices.smart_device import SmartDevice


class SmartLight(SmartDevice):

    def __init__(
        self,
        device_id,
        name,
        room,
        brightness=100,
        color_mode="White"
    ):

        super().__init__(device_id, name, room)

        self._brightness = brightness
        self._color_mode = color_mode

    def set_brightness(self, brightness):
        self._brightness = brightness

    def set_color_mode(self, color_mode):
        self._color_mode = color_mode

    def get_status(self):
        return (
            f"{self.name} | "
            f"Power: {'ON' if self.power_state else 'OFF'} | "
            f"Brightness: {self._brightness}% | "
            f"Color: {self._color_mode}"
        )
    
