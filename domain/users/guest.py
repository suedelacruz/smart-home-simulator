from domain.users.user import User


class Guest(User):

    def get_role(self):
        return "Guest"