# Conditional tests

# checking for equality
pizza = "delicious"
print("Is pizza disgusting? I predicit False.")
print(pizza == "disgusting")
print("Is pizza delicious? I predict True.")
print(pizza == "delicious")

# using the lower() method
animal = "Cat"
print("\nIs a cat an animal? I predicit True.")
print(animal.lower() == "cat")

# numerical tests 
age = 24
print("\nAre you already 25 years old?")
print(age >= 25)
print("But you are older than 18?")
print(age >= 18)

# tests using the and keyword and the or keyword
age = 18
gender = "male"
print("\nAre you at least 16 and female?")
print((age >= 16) and (gender == "female"))
print("Are you at least 16 or female?")
print((age >= 16) or (gender == "female"))

# checking if an item is (not) in a list
requested_toppings = ["salami", "pepperoni", "mushrooms"]
if "mushrooms" in requested_toppings:
    print("\nYou requested mushrooms.")
    print("We are sadly out of mushrooms right now!")
if "ice cream" not in requested_toppings:
    print("You requested ice cream as a topping for your pizza.")
    print("Are you crazy?")