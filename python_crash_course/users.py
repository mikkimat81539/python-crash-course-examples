""" Make a class called User Create two attributes called first_name and last_name, and then create several other
attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary
of the user’s information Make another method called greet_user() that prints a personalized greeting to the user
Create several instances representing different users, and call both methods for each user."""

class User:
    def __init__(self, first_name, last_name, age, location, user_name):
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"Username: {self.user_name}: Name: {self.first_name} {self.last_name} Age: {self.age} Location: {self.location}")

    def greet_user(self):
        print(f"Welcome {self.user_name}!!!")

profile = User("Mikaela", "Matthews", "24", "United States, TX", "Mikkimat5412")
profile.describe_user()
profile.greet_user()
