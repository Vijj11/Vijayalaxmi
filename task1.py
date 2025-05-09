users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

def add_user(new_user):
    users.append(new_user)
    print("User added.")

def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return "User not found."

def update_user(user_id, name=None, email=None):
    for user in users:
        if user["id"] == user_id:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            print("User updated.")
            return
    print("User not found.")

def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            print("User deleted.")
            return
    print("User not found.")

add_user({"id": 3, "name": "Charlie", "email": "charlie@example.com"})
print(get_user(2))     
update_user(1, name="Alice Smith")
delete_user(2)
