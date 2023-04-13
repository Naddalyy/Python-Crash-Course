# using dictionary in while loop
responses = {}
polling_active = True

while polling_active:
    # promt for the name and response
    name = input("\nWhat is your name? ")
    response = input(f"{name.title()}, if you could visit one place in the world, where would you go? ")

    # store response in dictionary
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':
        polling_active = False

print("\nThese are the results of the poll:")
for user, place in responses.items():
    print(f"{user.title()} would like to go to {place.title()}.")