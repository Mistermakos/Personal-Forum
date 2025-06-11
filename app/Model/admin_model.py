from Model.user_model import User

class Admin(User):
    def __init__(self, name, email):
        super().__init__(name,email)
