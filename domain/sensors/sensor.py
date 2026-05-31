from abc import ABC, abstractmethod


class Sensor(ABC):

    def __init__(self, sensor_id, name, room):

        self._id = sensor_id
        self._name = name
        self._room = room

        self._observers = []

    def add_observer(self, observer):

        self._observers.append(observer)

    def notify_observers(self, event):

        for observer in self._observers:
            observer.update(event)

    @abstractmethod
    def detect(self):
        pass