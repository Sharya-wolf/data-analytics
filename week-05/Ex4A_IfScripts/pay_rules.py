# ===========================================================================================
# Description: Continuing if scripts
# Author: Sha'Rya Weaver
# Date: 5/10/2026
# ============================================================================================
# create a script to calculate gross pay given the variables 
# pay_rate and hours_worked. If the person works more than 40 hours, pay the 
# overtime hours at 1.5 times the rate of regular hours.

pay_rate = eval(input("Please enter your pay rate.: "))
hours_worked = eval(input(" Please enter how many hours you wokred.: ")) 

if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = hours_worked * pay_rate

print("{'Pay rate:':<18} ${pay_rate:.2f}")
print(f"{'Hours worked:':<18} {hours_worked}")
print(f"{'Gross pay:':<18} ${gross_pay:.2f}")
# ---- Output ------------------------------------------------------------------------------------------------
# Please enter your pay rate.: 12.50

# Please enter how many hours you wokred.: 40

#{'Pay rate:':<18} ${pay_rate:.2f}

# Hours worked:      40

#Gross pay:         $500.00

















