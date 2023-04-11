# 3-8. Seeing the World

# 1. five places I want to visit the most
destination = ["scandinavia", "ireland", "australia", "united states", "canada"]

print("List in original order:")
print(destination)

# 2. use sorted() to print in alphabetical order
print("\nList in alphabetical order:")
print(sorted(destination))

# 3. reprinting to show that list is still in original order
print("\nShowing that the list is still in alphabetical order:")
print(destination)

# 4. use sorted() to print in reverse alphabetical order
print("\nList in reversed alphabetical order:")
print(sorted(destination, reverse=True))

# 5. reprinting to show that list is still in original order
print("\nShowing that the list is still in alphabetical order:")
print(destination)

# 6. use reverse() to change order of list
print("\nUsing reverse() on the list:")
destination.reverse()
print(destination)

# 7. using reverse() again to put list back in original order
print("\nUsing reverse() on the list:")
destination.reverse()
print(destination)

# 8. using sort() to store list in alphabetical order
print("\nUsing sort() to store list in alphabetical order:")
destination.sort()
print(destination)

print("\nUsing sort() to store list in reversed alphabetcial order:")
destination.sort(reverse=True)
print(destination)