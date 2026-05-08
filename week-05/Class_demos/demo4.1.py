# -----------------------------------------------------------------------------------------------------
# Sha'rya Weaver
# 5/8/2026
# Python Set
# -----------------------------------------------------------------------------------------------------

# unorderes 
my_set = {3, 1, 2}
print(my_set)
# ---------------------------------
# no duplicates
my_set = {1, 2, 3, 3, 3, 3}
print(my_set)
# ---------------------------------
# mutable
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)
# ---------------------------------
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)
# ---------------------------------
# Iteration
my_set = {1, 2, 3}
for item in my_set:
    print(item)
# ---------------------------------
#Unidexable
my_set = {1, 2, 3}

# ----------------------------------
# Class exercise
States = ("Ohio", "Alaska", "Virginia", "Pennsylvania", "Mississippi")
# Calculations
Longest_state = max(States, key=len)


print(f"Total number of states   :  {len(States)}")
print(f"Is Texas in the set?: {"Texas" in States}")
print(f"States in alphabetical order: {sorted(States)}")
print(f"Longest State name length: {Longest_state}")

# States.add("Georgia")
# print(f"Updated set after adding Georgia: {States}")

# States.discard("Ohio")
# print(f"Updated ste after removing Florida: {States}")

# Class Exercise 2

Day = int(input("Enter a number (1-7)"))

if Day == 1:
    print(f"Monday")

elif Day == 2:
    print(f"Tuesday")

elif Day == 3:
    print(f"Wednesday")

elif Day == 4:
    print("Thursday")

elif Day == 5:
    print(f"Friday")

elif Day == 6:
    print(f"saturday")

elif Day == 7:
    print(f"Sunday")

# Class Exercise 3

# ---- Initialise variables -----
total = 0
count = 0

print("Enter positive numbers one at a time ")
print("Enter a negative number to stop.\n")

# ---- Get first number ---------
number = eval(input("Enter a number: "))

# ---- While loop --- continues while number is positive --
while number >= 0:
    total  += number
    count  += 1
    number = float(input("Enter a number: "))

# ---- Display Results ----------
print(f"\numbers entered : {count}")
print(f"Sum            : {total:.2f}")

















