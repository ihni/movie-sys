from models import User

class UserService:
    def __init__(self):
        self.users = []

    def authenticate_email(self, email):
        '''check if valid email'''
        pass

    def is_duplicate_email(self, email):
        emails = [user.email for user in self.users]
        return email in emails

    def create_user(self, email) -> object:
        if self.is_duplicate_email(email):
            return False
        user = User(email)
        self.users.append(user)
        return user
    
    def find_user_by_email(self, email) -> object:
        for user in self.users:
            if user.email == email:
                return user
        return None
    
    def user_reservations(self, user):
        if user not in self.users:
            return False
        return user.reservations

    def list_users(self) -> list:
        return self.users
    
    def number_of_users(self) -> int:
        return len(self.users)