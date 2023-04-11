current_user = ["Nati", "Meekah", "Rechies", "Draro", "doneltopo"]
new_user = ["Ex", "Meekah", "DonElTopo", "v1olent", "cello"]

for i in range(len(current_user)):
    current_user[i] = current_user[i].lower()
for i in range(len(new_user)):
    new_user[i] = new_user[i].lower()

for user in new_user:
    if user in current_user:
        print(f"Sorry, {user.capitalize()}. You must choose another username!")
    else:
        print(f"{user.capitalize()} is an available username!")