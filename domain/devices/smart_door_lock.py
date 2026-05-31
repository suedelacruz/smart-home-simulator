from domain.devices.smart_device import SmartDevice


class SmartDoorLock(SmartDevice):

    def __init__(self, device_id, name, room):

        super().__init__(device_id, name, room)

        self._locked = True
        self._access_history = []

    def lock(self):
        self._locked = True

    def unlock(self, user="Unknown"):

        self._locked = False
        self._access_history.append(user)

    def get_status(self):

        return (
            f"{self.name} | "
            f"Locked: {self._locked}"
        )
    
    