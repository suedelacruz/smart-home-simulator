from domain.sensors.sensor import Sensor


class TemperatureSensor(Sensor):

    def __init__(
        self,
        sensor_id,
        name,
        room,
        temperature=22
    ):

        super().__init__(
            sensor_id,
            name,
            room
        )

        self._temperature = temperature

    def detect(self):

        print(
            f"Temperature changed in {self._room}"
        )

        self.notify_observers(
            "temperature_changed"
        )