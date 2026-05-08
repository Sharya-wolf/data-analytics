# Sha'Rya Weaver
# 5/7/2026

# How long will it take a savings account worth X to double in value based on an interest rate of IR?
# (Hint: Look up the "rule of 72")
      # a) Figure out the formula and what the script would look like, making up example values as needed.
      # b) Create the script

# Script:
Beginning_savings = 2098.22
interest_rate = 3.0

# Calculation
Years_to_double = 72 / interest_rate
Balance = Beginning_savings * 2

# Results
print(f"Your current savings is ${Beginning_savings:.2f}")
print(f"At a {format(interest_rate / 100, ".0%")} interest rate, your savings account will be worth ${format(Balance, ".2f")} in {format(Years_to_double, ".1f")} years.")

# Output: Your current savings is $2098.22. At a 3% interest rate, your savings account will be worth $4196.44 in 24.0 years.