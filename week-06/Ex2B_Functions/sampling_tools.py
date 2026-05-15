# ========================================================================================
# Description: Using library functions
# Sha'Rya Weaver
# 5/14/2026
# =========================================================================================
# Importing random module

import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

# 4c) The team wants to feature a "Product of the Day" based on one randomly selected
# item. Use random.choice() to select one product and print the result with an
# appropriate label. 

print("choice(products):", random.choice(products))
# First Output: Mouse
# Second Output: choice(products): Docking Station

# The different random output show the function is working as it should be giving random
# choices each time it is run.
# ----------------------------------------------------------------------------------------------
# 4b) Three products need to be selected for a brief usability survey. The same product
# should not appear more than once. Use random.sample() to select 3 items
# from products without replacement and print the results.

print("sample(products, k=3):", random.sample(products, k=3))
# Output: sample(products, k=3): ['Keyboard', 'Laptop', 'Desk Lamp']

# using the k=n will tell the systemn to only pick three random codes
# -----------------------------------------------------------------------------------------------
# 4c) For a presentation, all products should be displayed in a randomized order to
# avoid any appearance of ranking. Use random.shuffle() to shuffle the
# products list, then print the shuffled list.

random.shuffle(products)
print("shuffle(products):", products)
# ---- Output -------
# shuffle(products): ['Mouse', 'Headset', 'Surge Protector', 'Webcam', 'Laptop', 'USB Hub',
#                     'Keyboard', 'Monitor', 'Desk Lamp', 'Docking Station']
# -------------------------------------------------------------------------------------------------
# 4d) Use random.randint() to generate a simulated daily transaction count
# between 50 and 300, and print the result with a label.

print("Daily transaction count:", random.randint(50, 300))
# First Output: randint(50, 300): 247
# Second Output: Daily transaction count: 133
# Third Output: Daily transaction count: 83







































