from domain.sensors.sensor import Sensor


class MotionSensor(Sensor):

    def detect(self):

        print(f"Motion detected in {self._room}")

        self.notify_observers("motion_detected")