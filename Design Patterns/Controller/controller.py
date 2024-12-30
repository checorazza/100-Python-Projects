class UserModel:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email):
        self.users[username] = email

    def get_user(self, username):
        return self.users.get(username, "User not found")

#

class UserView:
    def show_user(self, username, email):
        print(f"Username: {username}, Email: {email}")

    def show_error(self, message):
        print(f"Error: {message}")

#

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

# Use

def main():
    model = UserModel()
    view = UserView()
    controller = UserController(model, view)

    controller.add_user("john_doe", "john@example.com")
    controller.get_user("john_doe")
    controller.get_user("jane_doe")

if __name__ == "__main__":
    main()
