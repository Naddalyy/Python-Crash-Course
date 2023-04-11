pizzas = ["salad pizza", "gyros pizza", "diavolo pizza"]

for pizza in pizzas:
    print("I like {}.".format(pizza))
print("I really love pizza!")



# 4-11. My Pizzas, Your Pizzas

friends_pizza = pizzas[:]
pizzas.append("salami pizza")
friends_pizza.append("funghi pizza")

print("My favourite pizzas are:")
for pizza in pizzas:
    print("- {}.".format(pizza.title()))

print("\nMy friend's favourite pizzas are:")
for pizza in friends_pizza:
    print("- {}.".format(pizza.title()))