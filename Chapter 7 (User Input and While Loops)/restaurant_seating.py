guests = input("For how many people would you like to book a table? ")
if int(guests) > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready!")