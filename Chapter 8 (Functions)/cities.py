def describe_cities(name, country='germany'):
    print(f"{name.title()} is a city in {country.title()}!")

describe_cities('münchen')
describe_cities(name='heidelberg')
# changing the default value
describe_cities('oulu', 'finland')