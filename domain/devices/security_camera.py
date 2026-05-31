from domain.devices.smart_device import SmartDevice


class SecurityCamera(SmartDevice):

    def __init__(self, device_id, name, room):

        super().__init__(device_id, name, room)

        self._recording = False
        self._motion_detection = True

    def start_recording(self):
        self._recording = True

    def stop_recording(self):
        self._recording = False

    def get_status(self):

        return (
            f"{self.name} | "
            f"Power: {'ON' if self.power_state else 'OFF'} | "
            f"Recording: {self._recording}"
        )
    
    