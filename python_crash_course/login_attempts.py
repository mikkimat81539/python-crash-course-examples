"""Add an attribute called login_attempts to your User class.
Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times.
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
Print login_attempts again to make sure it was reset to 0"""

class User:
    def __init__(self, first_name, last_name, age, location, user_name):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def greet_user(self):
        print(f"Welcome {self.user_name}!!!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Login attempts: {self.login_attempts + i}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login resets: {self.login_attempts + i} ")

for i in range(3):
    print(f"LOGIN")
    profile = User(input("Enter first name: "),
                   input("Enter last name: "),
                   int(input("Enter age: ")),
                   input("Enter location: "),
                   input("Enter username: "))

    profile.greet_user()

    profile.increment_login_attempts()
    profile.reset_login_attempts()
