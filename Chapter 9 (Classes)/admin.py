class User:
    """A simple attempt to represent a user."""
    def __init__(self, first_name, last_name, date_of_birth, username, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.date_of_birth = date_of_birth
        self.username = username
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Displaying a summary of the user's information."""
        full_name = f"{self.first_name} {self.last_name}"
        print(full_name)
        print(f" Username: {self.username}")
        print(f" Date of Birth: {self.date_of_birth}")
        print(f" Location: {self.location}")

    def greet_user(self):
        """Greeting the user."""
        msg = f"Welcome back, {self.username}!\n"
        print(msg)

    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Sets the value of login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, date_of_birth, username, location):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an administrator.
        """
        super().__init__(first_name, last_name, date_of_birth, username, location)
        # Creating a Privileges instance as an attribute
        self.privileges = Privileges()


class Privileges:
    """Initiliaze a very simple version of a privileges class."""
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user", "can unban user"]

    def show_privileges(self):
        """Prints the privileges of an administrator."""
        print("The administrator has the following privileges:")
        for priviledge in self.privileges:
            print(f"- {priviledge}")


admin = Admin('shigure', 'sohma', '26.01.1971', 'ShigU', 'japan')
admin.privileges.show_privileges()