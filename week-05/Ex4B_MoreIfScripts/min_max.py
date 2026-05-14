# =========================================================================
# Description: Showing the min and max using if/elif/else
# Sha'Rya Weaver
# Date: 5/10/2026
# =========================================================================

# 1. Create a script named min_max.py that displays both the smallest and then the
# largest of three numbers.

# Name your variables a, b, and c and assign them values. Then use if/else statements
# to determine and display the answer.

a = 12
b = 6
c = 23

# ---- Smallest -------
if a < b and a < c:
    smallest = a
elif b < a and b < c:
    smallest = b
else:
    smallest = c

# ---- Largest ---------

if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
else: 
    largest = c

print(f"The smallest value is {smallest}")
print(f"The largest value is {largest}")

# ---- Output ---------

# The smallest value is 6
# The largest value is 23






































