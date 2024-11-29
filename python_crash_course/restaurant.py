"""Make a class called Restaurant The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.

Three Restaurants: Start with your class from Exercise 9-1 Create three
different instances from the class, and call describe_restaurant() for each
instance."""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"the name of the restaurant is {self.restaurant_name} and they serve {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!!!")


for i in range(3):
    place = Restaurant(input("Enter a restaurant name: "), input("Enter a cuisine type: "))

    place.describe_restaurant()

    place.open_restaurant()