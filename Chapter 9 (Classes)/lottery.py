from random import choice

def choosing_winning_values(possible_values):
    """Chooses 4 values out of a list and adds them to a new list."""
    winning_values = []
    for x in range(4):
        x = choice(possible_values)
        winning_values.append(x)
    return winning_values

possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = choosing_winning_values(possible_values)
print(f"The winning ticket is: {winning_ticket}")