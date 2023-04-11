rivers = {
    'nile': 'egypt',
    'rhine': 'germany',
    'amazon': 'brazil',
    }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nThe dictionary contains the following rivers:")
for river in rivers.keys():
    print(river.title())

print("\nThe dictionary contains the following countries:")
for country in rivers.values():
    print(country.title())