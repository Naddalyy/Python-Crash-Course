prompt = "Please enter the desired topping for your pizza."
prompt += "\nEnter 'quit' once you are done! "

pizza_topping = ""
pizza = []

while pizza_topping != "quit":
    pizza_topping = input(prompt)
    if pizza_topping != "quit":
        print(f"Adding {pizza_topping} to your pizza...\n")
        pizza.append(pizza_topping)

print(f"Your pizza will have the following toppings: {pizza}")
    