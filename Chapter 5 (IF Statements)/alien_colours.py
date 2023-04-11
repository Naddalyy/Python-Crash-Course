# alien color 1
alien_color = "red"
if alien_color == "green":
    print("You have earned 5 points.")

alien_color = "green"
if alien_color == "green":
    print("You have earned 5 points.")

# alien color 2
alien_color = "red"
if alien_color == "green":
    print(f"You have earned 5 points. The alien is {alien_color}.")
elif alien_color == "yellow":
    print(f"You have earned 10 points. The alien is {alien_color}.")
else: 
    print(f"You have earned 15 points. The alien is {alien_color}.")