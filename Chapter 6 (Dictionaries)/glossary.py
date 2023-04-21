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
    'catchall statement': 'else block - matches any condition that is not matched by if or elif test',
    'function': 'named blocks of code designed to perform specific actions',
    'function call': 'execute code that is in the function',
    'modules': 'seperate files that help organizing main program files',
    'parameter': 'piece of information needed in functions',
    'argument': 'piece of information that is passed from a function call into a function',
    'positional arguments': 'need to be in the same order as the parameters',
    'keyword arguments': 'each argument consists of a name-value pair',
    'default values in functions': 'can be assigned for parameters, so argument in function call can be excluded',
    'return values': 'takes a value inside a function and sends it back',
    'slice notation [:]': 'makes a copy of a list',
    '*args': 'generic parameter name, which collects arbitrary postional arguments',
    '**kwargs': 'parameter name, used to collect nonspecific keyword arguments',
    'import statement': 'makes code from a module available in the current program file',
    'instance': 'object of a class',
    'instantiation': 'making an object from a class',
    'method': 'function that is part of a class',
    }

print("Glossary:")
for word, meaning in glossary.items():
    print(f"{word}: {meaning}\n")