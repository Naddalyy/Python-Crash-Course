class User:
    """A simple attempt to represent a user."""
    def __init__(self, first_name, last_name, date_of_birth, username, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.date_of_birth = date_of_birth
        self.username = username
        self.location = location.title()

    def describe_user(self):
        """Displaying a summary of the user's information."""
        full_name = f"{self.first_name} {self.last_name}"
        print(full_name)
        print(f" Username: {self.username}")
        print(f" Date of birth: {self.date_of_birth}")
        print(f" Location: {self.location}")

    def greet_user(self):
        """Greeting the user."""
        msg = f"Welcome back, {self.username}!\n"
        print(msg)

# Creating instances of the class and calling its methods
user_one = User("jenny", "miller", "23.04.2002", "J.Miller", "United States")
user_one.describe_user()
user_one.greet_user()

user_two = User("tim", "bill", "22.07.1976", "timbill", "Germany")
user_two.describe_user()
user_two.greet_user()

user_three = User("kyo", "sohma", "15.01.1983", "KyoCat", "Japan")
user_three.describe_user()
user_three.greet_user()