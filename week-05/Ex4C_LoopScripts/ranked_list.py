# ================================================================================================
# Description: Using Loops for Rankings
# Sha'Rya Weaver
# Date: 3/10/2026
# =================================================================================================

# Create a list of at least 5 items using anything you like: favorite foods, pets, cities you'd
# like to visit, skills you want to develop, etc.

pets = ["Dog", "Cat", "Birds", "snake", "turtles", "fishes"]

for i, animals in enumerate(pets, start = 1):
    if i == 1:
        print(f"{i}. {animals} <- top pick!")
    else:
        print(f"{i}. {animals}")

# ---- Output -------

# 1. Dog <- top pick!
# 2. Cat
# 3. Birds
# 4. snake
# 5. turtles
# 6. fishes

















































