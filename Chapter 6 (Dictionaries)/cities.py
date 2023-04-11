cities = {
    'brilon': {
        'country': 'germany',
        'population': '26000',
        'twin town': 'herbolzheim',
        },
    
    'augsburg': {
        'country': 'germany',
        'population': '295000',
        'twin town': 'amagasaki',
        },

    'copenhagen': {
        'country': 'denmark',
        'population': '602000',
        'twin town': 'trzcianka',
        },

    }

for name, information in cities.items():
    country = information['country'].title()
    population = information['population']
    twin_town = information['twin town'].title()
    print(f"{name.title()} is a city in {country}.\n"
          f"Its approximate population is {population} people.\n"
          f"The twin town is {twin_town.title()}.\n")