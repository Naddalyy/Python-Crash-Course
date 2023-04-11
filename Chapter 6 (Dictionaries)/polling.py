favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

poll_participants = ['sarah', 'kasper', 'nathalie', 'jess', 'phil']

for participant in poll_participants:
    if participant in favorite_languages.keys():
        print(f"Thank you for your response, {participant.title()}.")
    else:
        print(f"Please consider taking the poll, {participant.title()}!")