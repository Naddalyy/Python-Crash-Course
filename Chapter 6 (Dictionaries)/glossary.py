glossary = {
    'key-value pair': 'used in dictionaries, each key is connected to a value',
    'immutable/mutable': 'not changeable/changeable',
    'variable': 'a value you assign data to',
    'conditional test': 'evaluates to True or False',
    'tuple': 'immutable item that can contain multiple values',
    'set': 'a collection in which each item must be unique/not doubled',
    'for loop': 'iterates through each item in a list/set/dictionary/..',
    'dictionary': 'contains key-value pairs, much like an actual dictionary',
    'list': 'can contain multiple items that are mutable',
    'catchall statement': 'else block - matches any condition that is not matched by if or elif test'
    }

print("Glossary:")
for word, meaning in glossary.items():
    print(f"{word}: {meaning}\n")