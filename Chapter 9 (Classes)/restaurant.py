class Restaurant:
    """A simple model for a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Simply describes the restaurant."""
        print(f"{self.restaurant_name} offers real good {self.cuisine_type} food.")

    def open_restaurant(self):
        """Prints a statement that the restaurant opens."""
        print(f"{self.restaurant_name} is now open!")


# Creating an instance of the class, printing both attributes and calling both methods
restaurant = Restaurant("covaccino", "italian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()   


# 9-2. Creating more instances of the class and calling the describe method
restaurant_one = Restaurant("tokyos taste", "japanese")
restaurant_two = Restaurant("paderborner brauhaus", "german")

restaurant_one.describe_restaurant()
restaurant_two.describe_restaurant()