class UserModel:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email):
        self.users[username] = email

    def get_user(self, username):
        return self.users.get(username, "User not found")
