# Sha'Rya Weaver
# Date: 5/52026


# Sample Problem: How do you calculate the total due at a resturant given the food cost, tax, and tip?
# Formula: Total Due is determined by: Food Cost + Tax + Tip
# Script: 

# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results
print("The total due is " + str(total_due)) # The total due is $97.79
# The string fuction is any text/characters enclosed in quotation marks.
# Because "The total due is" is enclosed in quotation marks it is considered a string.

print("Food cost is " + str(food_cost) + " and tax is" + str(tax)) # Food cost is 79.25 and tax is 6.54
print ("Tip is " + str(tip)) # Tip is 12.0
print ("Total due is " + str(total_due)) # Total due is 97.79

print ("Tip is " + format (tip, ".2f")) # Tip is 12.00
# Format function is used to format data as a string so we don't need to include the str() function with it.