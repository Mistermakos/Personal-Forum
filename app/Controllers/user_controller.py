from Models.user_model import User

def get_all_users():
    return User.get_all()

def get_user(user_id):
    return User.get_by_id(user_id)

def create_user(data):
    user = User(data.get('name'), data.get('password'), data.get('email'))
    user.save()
    return user

def update_user(user_id, data):
    user = User.get_by_id(user_id)
    if not user:
        return None
    user.name = data.get('name', user.name)
    user.password = data.get('password', user.password)
    user.email = data.get('email', user.email)
    user.save()
    return user

def delete_user(user_id):
    User.delete(user_id)
