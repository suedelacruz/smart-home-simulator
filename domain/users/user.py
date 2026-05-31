from abc import ABC


class User(ABC):

    def __init__(
        self,
        user_id,
        name
    ):

        self._id = user_id
        self._name = name

    @property
    def name(self):
        return self._name