from domain.sensors.sensor import Sensor


class DoorSensor(Sensor):

    def detect(self):

        print(
            f"Door opened in {self._room}"
        )

        self.notify_observers(
            "door_opened"
        )