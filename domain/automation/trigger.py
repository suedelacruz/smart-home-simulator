from abc import ABC


class Trigger(ABC):

    def __init__(self, event_name):

        self._event_name = event_name

    @property
    def event_name(self):

        return self._event_name