# ===========================================================================================================
# Description: Using match/case as another way instead of if
# Sha'Rya weaver
# Date: 5/10/2026
# ===========================================================================================================
# rewrite it using a match/case statement instead of if/elif/else

# 1 Marketing
# 5 Human Resources
# 10 Accounting
# 12 Legal
# 18 IT
# 20 Customer Relations

dept_code = eval(input("Please enter your department code: "))

match dept_code:
    case 1:
        print("Marketing is your department!")
    case 5:
        print("Human Resources is your department!")
    case 10:
        print("Accounting is your department!")
    case 12:
        print("Legal is your department!")
    case 18:
        print("IT is your department!")
    case 20:
        print("Customer Relations is your department")
    case _: 
        print("Code not found. Please try again.")

# Output: Please enter your department code: 13 Code not found. Please try again.

# Output: Please enter your department code: 10 Accounting is your department!

# Both is very similar and both give the same outcome. In turns of using the if/elif/else
# I would say it's easier to explain and understand although match/case is quicker and easier
# to type. With good enough explaining it can be easy to follow and understand.

















