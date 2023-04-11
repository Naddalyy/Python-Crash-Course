# 3-3. Your own list: Think of your favorite mode of transportation, such as motorcycle or car, and make a list that stores several
# examples. Use your list to print a series of statements about these items.

cars = ["audi", "bmw", "volkswagen", "mercedes"]

msg = "Lars owns an {}.".format(cars[0].title())
print(msg)

msg = "{} makes beautiful cars.".format(cars[1].upper())
print(msg)

msg = "I own a {} for several years already.".format(cars[2].title())
print(msg)

msg = "Noone can afford a {}.".format(cars[3].title())
print(msg)