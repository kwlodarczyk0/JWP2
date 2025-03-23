class UserNotFoundError(Exception):
    pass

class WrongPasswordError(Exception):
    pass

class UserAuth:
    def __init__(self, users):
        self.users = users

    def login(self, username, password):
        if username not in self.users:
            raise UserNotFoundError("User not found")
        if username in self.users and self.users[username] != password:
            raise WrongPasswordError("Wrong password")
        return True

auth = UserAuth({"admin": "1234", "user": "abcd"})

try:
    auth.login("admin", "1234")
    #auth.login("unknown", "passs")
    #auth.login("user", "wrongpass")
except Exception as e:
    print(f"Błąd: {e}")