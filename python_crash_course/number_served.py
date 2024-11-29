""" Start with your program from restaurant.
Add an attribute called number_served with a default value of 0.
Create an instance called restaurant from this class.
Print the number of customers the restaurant has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of customers that have been served.
Call this method with a new number and print the value again.

Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
Call this method with any number you like that could represent how many customers were served in, say, a
day of business"""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.default_value = number_served

    def describe_restaurant(self):
        print(f"the name of the restaurant is {self.restaurant_name} and they serve {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!!!")

    def number_served(self):
        self.default_value = 0

    def increment_number_served(self):
        self.additional_customers = int(input("Enter the number of additional customers: "))
        print(f"There was {self.additional_customers + self.default_value} customers served at the end of business.")


restaurant = Restaurant(input("Enter a restaurant name: "),
                        input("Enter a cuisine type: "),
                        int(input("Enter the number of customers served in the morning: ")))

restaurant.describe_restaurant()

restaurant.open_restaurant()

restaurant.increment_number_served()
