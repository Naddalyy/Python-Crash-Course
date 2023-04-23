from random import randint

class Die:
    """A die that can be rolled."""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Rolls the dice between 1 and the number of sides."""
        return randint(1,self.sides)

# Rolling a d6
d6 = Die()
results = []
for number in range(10):
    result = d6.roll_die()
    results.append(result)
print("Rolling a d6 ten times:")
print(results)

# Rolling a d10
d10 = Die(10)
results = []
for number in range(10):
    result = d10.roll_die()
    results.append(result)
print("Rolling a d10 ten times:")
print(results)

# Rolling a d20
d20 = Die(20)
results = []
for number in range(10):
    result = d20.roll_die()
    results.append(result)
print("Rolling a d20 ten times:")
print(results)