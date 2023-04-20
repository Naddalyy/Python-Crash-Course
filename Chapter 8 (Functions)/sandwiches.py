def make_sandwich(*ingredients):
    """Function that accepts an arbitary number of arguments."""
    print("Making your sandwich:")
    for ingredient in ingredients:
        print(f"Adding {ingredient} to your sandwich...")
    print("Finished making your sandwich!\n")

make_sandwich("cucumber", "salad")
make_sandwich("salad", "chicken", "salt")
make_sandwich("tomatoes")