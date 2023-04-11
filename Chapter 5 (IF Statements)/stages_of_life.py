age = 66
if age < 2:
    life_stage = "baby"
elif age < 4:
    life_stage = "toddler"
elif age < 13:
    life_stage = "kid"
elif age < 20:
    life_stage = "teenager"
elif age < 65:
    life_stage = "adult"
else:
    life_stage = "elder"

if life_stage == "adult" or life_stage == "elder":
    print(f"You are an {life_stage}.")
else:
    print(f"You are a {life_stage}.")
