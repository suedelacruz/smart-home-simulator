from domain.devices.smart_device import SmartDevice


class SmartSpeaker(SmartDevice):

    def __init__(
        self,
        device_id,
        name,
        room,
        volume=50
    ):

        super().__init__(device_id, name, room)

        self._volume = volume
        self._playing_music = False

    def play_music(self):
        self._playing_music = True

    def stop_music(self):
        self._playing_music = False

    def set_volume(self, volume):
        self._volume = volume

    def get_status(self):

        return (
            f"{self.name} | "
            f"Power: {'ON' if self.power_state else 'OFF'} | "
            f"Volume: {self._volume} | "
            f"Playing: {self._playing_music}"
        )
    

    