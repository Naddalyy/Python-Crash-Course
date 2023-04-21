class Restaurant:
    """A simple model for a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant."""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Simply describes the restaurant."""
        print(f"{self.restaurant_name} offers real good {self.cuisine_type} food.")

    def open_restaurant(self):
        """Prints a statement that the restaurant opens."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        """Set the number of customers served to a given value."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Increment the number of customers served with a given value."""
        self.number_served += additional_served



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


# 9-4. Number Served
# Adding a default value to the class and changing it directly
print(f"{restaurant.restaurant_name} has served {restaurant.number_served} customers...")
restaurant.number_served = 59
print(f"Now {restaurant.restaurant_name} has served {restaurant.number_served} customers...")

# Setting a new value through a method
restaurant.set_number_served(217)
print(f"Now {restaurant.restaurant_name} has served {restaurant.number_served} customers...")

# Incrementing through a method
restaurant.increment_number_served(10)
print(f"Now {restaurant.restaurant_name} has served {restaurant.number_served} customers...")