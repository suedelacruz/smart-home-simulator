from domain.users.user import User


class Technician(User):

    def get_role(self):
        return "Technician"