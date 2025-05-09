import hashlib

users = {}  

def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def register(username, password):
    if username in users:
        print("User already exists.")
    else:
        users[username] = hash_pw(password)
        print("Created new user")

def login(username, password):
    if users.get(username) == hash_pw(password):
        print("Login Successful")
    else:
        print("Invalid username or password")


register("john", "mypassword")
login("john", "mypassword")
