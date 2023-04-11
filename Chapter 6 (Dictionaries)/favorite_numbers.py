favorite_numbers = {
    'kasper': [13, 16, 300],
    'tero': [11, 13, 2334234],
    'lorenz': [77, 89, 3423],
    'nathalie': [14, 21, 101],
    'michelle': [5, 301, 311, 22],
    }

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers[:-1]:
        print(f"{number}, ", end = "")
    print("and", numbers[-1], "\n")