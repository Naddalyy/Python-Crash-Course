# 3-4. Guest List: Make a list that includes at least three people you'd like to invite to dinner. Then use your list to print a 
# message to each person, inviting them to dinner.

invited_guests = ["Michelle", "Karl-Heinz", "Irmgard"]

print("Invitations:")
msg = f"Dear {invited_guests[0]}, I would like to invite you to my dinner party."
print(msg)
msg = f"Dear {invited_guests[1]}, I would like to invite you to my dinner party."
print(msg)
msg = f"Dear {invited_guests[2]}, I would like to invite you to my dinner party."
print(msg)


# 3-5. Changing Guest List: Add a print() call at the end of your program, stating the name of the guest who can't make it.
# Modify your list, replacing the name of the guest who can't make it with the new name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

print("\nNews:")
print(f"{invited_guests[1]} sadly can't make it to the party.\n")

invited_guests[1] = "Wenke"

print("New invitations:")
msg = f"Dear {invited_guests[0]}, I would like to invite you to my dinner party."
print(msg)
msg = f"Dear {invited_guests[1]}, I would like to invite you to my dinner party."
print(msg)
msg = f"Dear {invited_guests[2]}, I would like to invite you to my dinner party."
print(msg)


# 3-6. More Guests: Add a print() call at the end of the function, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitations messages, one for each person in your list.

print("\nNews:")
print("Hey everyone! I found a bigger table, so more people will be joining us.\n")

invited_guests.insert(0, "Jan")
invited_guests.insert(2, "Tino")
invited_guests.append("Lilly")

print("New invitations:")
msg = f"Dear {invited_guests[0]}, I would like to invite you to my dinner party."
print(msg)
msg = f"Dear {invited_guests[1]}, I would like to invite you to my dinner party."
print(msg)
msg = f"Dear {invited_guests[2]}, I would like to invite you to my dinner party."
print(msg)
msg = f"Dear {invited_guests[3]}, I would like to invite you to my dinner party."
print(msg)
msg = f"Dear {invited_guests[4]}, I would like to invite you to my dinner party."
print(msg)
msg = f"Dear {invited_guests[5]}, I would like to invite you to my dinner party."
print(msg)


# 3-7. Shrinking Guest List: Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list,
# print a message to that person letting them know you're sorry you can't invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they're still invited.
# Use del to remove the last two names from your list, so you can have an empty list. Print your list to make sure you actually have an
# empty list at the end of your program.

print("\nNews:\nPlans have changed! I can invite only two guests for dinner.\n")

popped_guest = invited_guests.pop(0)
print(f"I am sorry, {popped_guest}. I can't invite you to dinner.")

popped_guest = invited_guests.pop(1)
print(f"I am sorry, {popped_guest}. I can't invite you to dinner.")

popped_guest = invited_guests.pop(1)
print(f"I am sorry, {popped_guest}. I can't invite you to dinner.")

popped_guest = invited_guests.pop(2)
print(f"I am sorry, {popped_guest}. I can't invite you to dinner.")

print(f"{invited_guests[0]}, you are still invited to join me for dinner.")
print(f"{invited_guests[1]}, you are still invited to join me for dinner.")

del invited_guests[0]
del invited_guests[0]
print(invited_guests)

# 3-9. Dinner Guests: Use len() to print a message indicating the number of people you're inviting to dinner.

guests = ["Michelle", "Irmgard", "Wenke", "Lilly"]
print("I am inviting {} guests to dinner.".format(len(guests)))