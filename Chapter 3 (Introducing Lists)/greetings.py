# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just print each person's name, print a message to them.
# The text of each message should be the same, but each message should be personalized with the person's name.

names = ["Jonas", "Hodor", "Kasper", "Tero"]

msg = "Hi, {}. I hope you are doing alright!".format(names[0])
print(msg)

msg = "Hi, {}. I hope you are doing alright!".format(names[1])
print(msg)

msg = "Hi, {}. I hope you are doing alright!".format(names[2])
print(msg)

msg = "Hi, {}. I hope you are doing alright!".format(names[3])
print(msg)