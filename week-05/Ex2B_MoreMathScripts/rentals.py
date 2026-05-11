# ========================================================================================================
# Sha'Rya Weaver
# 5/8/2026
# ========================================================================================================
# There are X people going on a tour. Carter vans seat 15 passengers each. Vans cost $250
# per day to rent(including the driver's pay). How many vans do you need? How much will it
# cost to rent vans? what is the cost if you split it per person?
# ========================================================================================================
# Test your script with 38 tourists. Now do some seperate calculations to check your work:
   # a) How much money did your script say you had to charge per person?
   # b) If you multiply that out, how much did you collect?
   # c) How much were the vans?
   # d) Why do you have leftover money?
# =========================================================================================================
# Script
Tourists = 38
Capacity = 15
Van_cost = 250

# Calculations
from math import ceil

Vans_needed = ceil(Tourists / Capacity)
Total_cost = Vans_needed * Van_cost 
per_person = Total_cost / Tourists

# Results
print(f"The number of vans needed is {Vans_needed}")
print(f"The total cost to rent the vans is ${Total_cost:.2f}")
print(f"The cost per person is ${per_person:.2f}")

# Output
# The number of vans needed is 3
# The total cost to rent the vans is $750.00
# The cost per person is $19.74








