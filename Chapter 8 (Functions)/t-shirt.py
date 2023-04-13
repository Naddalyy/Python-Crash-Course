def make_shirt(size='L', text='I love Python!'):
    print(f"""We are making a shirt in the size {size.upper()}.
We will print the following text on it: '{text}'\n""")

# using default values to call
make_shirt()
# changing one default value
make_shirt(size='m')

# using positional arguments to call
make_shirt('m', 'Never give up!')
# using keyword arguments to call
make_shirt(size='xxl',text='Believe you can and you are halfway there.')