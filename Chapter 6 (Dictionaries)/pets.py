# creating an empty list
pets = []

# dicts about pets
pet = {
    'name': 'whis',
    'kind': 'cat',
    'owner': 'nathalie',
    }
pets.append(pet)

pet = {
    'name': 'beerus',
    'kind': 'cat',
    'owner': 'nathalie',
    }
pets.append(pet)

pet = {
    'name': 'lilly',
    'kind': 'dog',
    'owner': 'michelle'
    }
pets.append(pet)

pet = {
    'name': 'eddy',
    'kind': 'hamster',
    'owner': 'michelle',
    }
pets.append(pet)

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['kind']} and its owner is {pet['owner'].title()}.")

# a bit more fancy for loop/print statement
for pet in pets:
    print(f"\nHere is what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        if key == 'kind':
            print(f"{key}: {value}")
        else:
            print(f"{key}: {value.title()}")