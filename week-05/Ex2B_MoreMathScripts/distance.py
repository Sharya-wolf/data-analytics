# 
# Sha'Rya Weaver
# 5/7/2026

# How do you calculate the distance between coordinates (x1, y1) and (x2, y2)?
# Hint: (You'll need to look up how to calculate a square root in Python, which may involve a function from the math module)
# Formula: squareroot((x2 - x1)**2 + (y2 - y1)**2)

# Script
x1 = 4
x2 = 5
y1 = 8
y2 = 9

# Calculations
from math import sqrt

Distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Results
print(f"The distance btwwen the cordinates is {Distance:.2f}")

# Output
# The distance between the cordinates is 1.41.










