from user_model import UserModel
from user_view import UserView
from user_controller import UserController

def main():
    model = UserModel()
    view = UserView()
    controller = UserController(model, view)

    controller.add_user("john_doe", "john@example.com")
    controller.get_user("john_doe")
    controller.get_user("jane_doe")

if __name__ == "__main__":
    main()
