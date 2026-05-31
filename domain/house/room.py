class Room:

    def __init__(
        self,
        name
    ):

        self._name = name
        self._devices = []

    def add_device(
        self,
        device
    ):

        self._devices.append(device)

    @property
    def name(self):
        return self._name

    @property
    def devices(self):
        return self._devices