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

# Creating a child class that inherits from the Restaurant class
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["strawberry", "raspberry", "chocolate"]

    def display_flavors(self):
        """Prints the different ice cream flavors."""
        print(f"{icecreamstand.restaurant_name} offers the following ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

icecreamstand = IceCreamStand("Eis-Café Venezia", "italian")
icecreamstand.display_flavors()