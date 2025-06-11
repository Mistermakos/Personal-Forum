from hashlib import sha3_512
with open("salt.txt") as mess:
    salt = mess.read()

def login(name: str, password: str):
    # check if name and sha3_512(salt+password) matches that of SQL
    return True

