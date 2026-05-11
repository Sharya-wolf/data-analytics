#
# Sha'Rya Weaver
# 5/7/2026

# Federal taxes are 23% of your salary every month. You make X amount of money.
# How much is withheld for taxes?
   # ( Make sure not display partial cents in your results! Experiment with using 
   # either the round() function or format() method to get results to display to two 
   # decimal places.)

# Script
Monthly_salary = 386.93
Tax_rate = 23

# Calculations
Tax_withheld = round(Monthly_salary * (Tax_rate / 100), 2)

# Results
print(f"My monthly salary is {Monthly_salary:.2f}")
print(f"Federal taxes are {Tax_rate}%")
print(f"The amount withheld for federal taxes is ${Tax_withheld:.2f}")

# Output
# My monthly salary 386.93
# Federal taxes are 23%
# The amount withheld for federal taxes is $88.99

