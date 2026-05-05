
class User:
    total_users = 0

    def __init__(self, username, password):

        if not isinstance(username, str) or not username.strip() or not len(password.strip()) >= 5:
            raise ValueError

        self.username = username.strip()
        self.password = password.strip()
        User.total_users += 1


    @staticmethod
    def get_total():
        return User.total_users


    def __str__(self):
        return f"User: {self.username}"


#-----------------------------------------------------------------------------------------------------------------------


try:
    user = User("VLad", "123")

except ValueError:
    print("Slovilo")

try:
    user2 = User("     ", "123456")

except ValueError:
    print("Slovilo pustogo")

try:
    user3 = User(123, "12345")

except ValueError:
    print("Slovilo username")

user4 = User("  Oleh ", "12345")

print(User.get_total())
print(user4)
