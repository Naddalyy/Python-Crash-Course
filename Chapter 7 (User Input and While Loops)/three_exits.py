# using conditional test to stop the loop 
current_number = 0
while current_number <= 9:
    current_number += 1
    print(current_number)

# using an active variable to stop the loop
prompt = "Tell me something, and I will repeat it back to you. "
prompt += "Enter 'quit' to close the program.\n"
active = True
while active:
    message = (input(prompt))
    if message.lower() == 'quit':
        active = False
    else:
        print(message)

# using break to stop the loop
prompt = "Name your favorite place to store it in a list!\n"
prompt += "Enter 'quit' once you are done.\n"
favorite_places = []
while True:
    place = (input(prompt))
    if place.lower() == 'quit':
        print(f"Your favorite places are: {favorite_places}")
        break
    else:
        favorite_places.append(place)
        print("Is there another place?")