animals = ["cat", "tiger", "lion", "puma", "gepard", "leopard"]

for animal in animals:
    print("A {} is a feline.".format(animal))
print("All these animals are felines.")


# 4-10. Slices
print("The first three items in this list are:")
print(animals[:3])

print("\nThe items for the middle of the list are:")
print(animals[2:4])

print("\nThe last three items in the list are:")
print(animals[-3:])