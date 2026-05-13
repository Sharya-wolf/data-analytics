# =================================================================================================================
# Description: More if script pratices
# Author: Sha'Rya weaver
# Date: 5/10/2026
# =================================================================================================================
# Write a script named dept_converter.py that uses if/elif/else logic to determine
# and print department name based on a department code. Make sure to test your script with multiple codes.
# 1 Marketing
# 5 Human Resources
# 10 Accounting
# 12 Legal
# 18 IT
# 20 Customer Relations
dept_code = int(input("Please enter your departent code: "))

if dept_code == 1:
    print("Marketing is your department!")
elif dept_code == 5:
    print("Human Resources is your department!")
elif dept_code == 10:
    print("Accounting is your department!")
elif dept_code == 12:
    print("Legal is your department!")
elif dept_code == 18:
    print("IT is your department!")
elif dept_code == 20:
    print("Customer Relations is your department!")
else:
    print("Code not found. Please try again.")

# Output: Please enter your departent code: 13 Code not found. Please try again

# Output: Please enter your departent code: 10 Accounting is your department!










































