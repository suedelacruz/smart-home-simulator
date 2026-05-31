from abc import ABC, abstractmethod


class SmartDevice(ABC):

    def __init__(self, device_id, name, room, energy_consumption=0):

        self._id = device_id
        self._name = name
        self._room = room
        self._power_state = False
        self._energy_consumption = energy_consumption

    def turn_on(self):
        self._power_state = True

    def turn_off(self):
        self._power_state = False

    @abstractmethod
    def get_status(self):
        pass

    @property
    def name(self):
        return self._name

    @property
    def room(self):
        return self._room

    @property
    def power_state(self):
        return self._power_state
    
    @property
    def energy_consumption(self):
        return self._energy_consumption
    
    
    

    

   