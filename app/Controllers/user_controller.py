from Model.user_model import User
from Model.admin_model import Admin
from hashlib import sha3_512
with open("salt.txt") as mess:
    salt = mess.read()

def add_new_User(name: str, password: str, email: str):
    #check if such user does not exit
        #check if email is taken
            #chceck if password meets requirements (we have standards after all!)
                #new_user = User(name = name, email = email, password = password)
                # we encrypt passwords with salt(set in .txt file)+password, and that is encrypted
    return "Added new User"

def add_new_Admin(UserId:int):
    #chceck if such user exists
        #check if user is not already an admin
            #grant admin privliges
    return "Added new admin"

def delete_user(postId: int, userId: int, comment: str):
    #check if such user exists    
    return "deleted user"

def delete_admin(adminId: str):
    #Check if such admin is indeed admin
    return "deleted admin"