# dict about a person
person_0 = {
    'first_name': 'michelle',
    'last_name': 'laumann',
    'age': '18',
    'city': 'brilon',
    }

print(f"{person_0['first_name'].title()} {person_0['last_name'].title()} is {person_0['age']} years old.")
print(f"She lives in {person_0['city'].title()}.\n")

# more dicts about people
person_1 = {
    'first_name': 'dirk',
    'last_name': 'hoffmann',
    'age': '27',
    'city': 'augsburg',
    }
person_2 = {
    'first_name': 'nathalie',
    'last_name': 'suckfiel',
    'age': '24',
    'city': 'bontkirchen',
    }

# list of dicts
people = [person_0, person_1, person_2]
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
    print(f"{name} is {age} old and lives in {city}.")