age = int(input("How old are you? "))

if age < 3:
    print("The ticket is free!")
elif age < 13:
    print("The ticket costs $10.")
else:
    print("The ticket costs $15.")