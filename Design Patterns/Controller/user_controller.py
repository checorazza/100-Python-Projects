from user_model import UserModel
from user_view import UserView

class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_user(self, username, email):
        self.model.add_user(username, email)

    def get_user(self, username):
        user = self.model.get_user(username)
        if user == "User not found":
            self.view.show_error(user)
        else:
            self.view.show_user(username, user)
