sandwich_orders = ['breakfast roll', 'fluffernutter', 'pastrami', 'mettbrötchen', 'hot chicken sandwich',
                   'maxwell street polish', 'pastrami', 'pambazo', 'grinder', 'pastrami']
finished_sandwiches = []

print(f"Sandwich orders: {sandwich_orders}\n")
print("Sorry, but the deli has run out of pastrami today!\n")
# removing pastrami from list of sandwich orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# moving order to finished list
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I am working on your {sandwich.title()}.")
    finished_sandwiches.append(sandwich)

# printing the finished list
print(f"\nThe following sandwiches have been finished:")
for sandwich in finished_sandwiches:
    print(f"I finished making your {sandwich.title()}!")