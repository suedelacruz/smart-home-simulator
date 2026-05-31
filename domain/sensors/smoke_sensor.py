from domain.sensors.sensor import Sensor


class SmokeSensor(Sensor):

    def detect(self):

        print(f"Smoke detected in {self._room}")

        self.notify_observers(
            "smoke_detected"
        )