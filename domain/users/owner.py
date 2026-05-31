from domain.users.user import User


class Owner(User):

    def get_role(self):
        return "Owner"
    
    