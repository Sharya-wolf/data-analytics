# ===============================================================================================================
# Description: Working with Tuples & Sets
# Author: Sha'Rya Weaver
# Date: 5/9/2026
# ===============================================================================================================
# ---------------------------------------------------------------------------------------------------------------
# Start by creating two tuples: one that lists at least 3 types of candy that can come in
# fruit flavors, and another that lists at least 3 fruity flavors. (Feel free to get creative with
# your flavor ideas...)

Candy = ("lollipops", "Jolly Ranchers", "Ring Pop")
Flavors = ("Watermelon", "Grape", "Blue Rasberry")
# ---------------------------------------------------------------------------------------------------------------
# create a new variable to store candy combinations as a set. Using the index of
# each tuple, add at least one combination of each candy and flavor to the new set – for
# example, putting together tuple1[0] and tuple2[1

candy_combinations = set()

candy_combinations.add(Candy[0] + " with " + Flavors[0])
candy_combinations.add(Candy[1] + " with " + Flavors[1])
candy_combinations.add(Candy[2] + " with " + Flavors[2])

# Create an output message that says, “Today’s candy options include:” and then prints
# the contents of the set.

print("Today's candy options include:")  # Output: Today's candy options include:

print(candy_combinations) # Output: {'Jolly Ranchers with Grape', 'Ring Pop with Blue Rasberry', 'lollipops with Watermelon'}
# ------------------------------------------------------------------------------------------------------------------
# Print the output multiple times. What do you notice about the order of the items as you
# repeat the output?
print("Today's candy options include:")
print(candy_combinations)
# Output: Today's candy options include:
# Output: {'Jolly Ranchers with Grape', 'lollipops with Watermelon', 'Ring Pop with Blue Rasberry'}

print("Today's candy options include:")
print(candy_combinations)
# Output: Today's candy options include:
# Output: {'Jolly Ranchers with Grape', 'lollipops with Watermelon', 'Ring Pop with Blue Rasberry'}

print("Today's candy options include:")
print(candy_combinations)
# Output: Today's candy options include:
# Output: {'Jolly Ranchers with Grape', 'lollipops with Watermelon', 'Ring Pop with Blue Rasberry'}

print("Today's candy options include:")
print(candy_combinations)
# Output: Today's candy options include:
# Output: {'Jolly Ranchers with Grape', 'lollipops with Watermelon', 'Ring Pop with Blue Rasberry'}

# From what I have noticed the set stays the same but when you run it again the order changes. 
# Although once it changes it stays in that order.










