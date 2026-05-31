class House:

    def __init__(self):

        self._rooms = []
        self._users = []
        self._rules = []

    def add_room(
        self,
        room
    ):

        self._rooms.append(room)

    def add_user(
        self,
        user
    ):

        self._users.append(user)

    def add_rule(
        self,
        rule
    ):

        self._rules.append(rule)

    @property
    def rooms(self):
        return self._rooms

    @property
    def users(self):
        return self._users

    @property
    def rules(self):
        return self._rules