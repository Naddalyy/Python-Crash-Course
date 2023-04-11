favorite_places = {
    'kasper': ['Copenhagen', 'Germany'],
    'michelle': ['in the forest', 'at school', 'at home'],
    'nathalie': ['in the sun', 'dreamland'],
    }

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"- {place}")