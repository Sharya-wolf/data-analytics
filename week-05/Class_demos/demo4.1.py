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
print(my_set[0])
# ----------------------------------
# Class exercise
States = ("Ohio", "Alaska", "Virginia", "Pennsylvania", "Mississippi")
# Calculations
Longest_state = max(States, key=len)


print(f"Total number of states   :  {len(States)}")
print(f"Is Texas in the set?: {"Texas" in States}")
print(f"States in alphabetical order: {sorted(States)}")
print(f"Longest State name length: {Longest_state}")

States.add("Georgia")
print(f"Updated set after adding Georgia: {States}")

States.discard("Ohio")
print(f"Updated ste after removing Florida: {States}")





















