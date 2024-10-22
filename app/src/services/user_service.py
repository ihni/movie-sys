from models import User

class UserService:
    def __init__(self):
        self.users = []

    def create_user(self, email) -> object:
        user = User(email)
        self.users.append(user)
        return user
    
    def find_user_by_email(self, email) -> object:
        for user in self.users:
            if user.email == email:
                return user
        return None
    
    def list_users(self) -> list:
        return self.users
    
    def number_of_users(self) -> int:
        return len(self.users)