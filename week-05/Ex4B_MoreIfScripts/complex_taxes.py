# ===============================================================================================
# Description: Complex if/elif/else
# Sha'Rya Weaver
# Date: 5/10/2026
# ===============================================================================================
# -----------------------------------------------------------------------------------------------
# 1. Create a script named complex_taxes.py that will calculate federal tax based on the
# values of annual gross income (a number) and a filing status (‘single’ or ‘joint’).

# 2. Start by copying your code for calculation of gross pay from the earlier lab
# (pay_rules.py) and include it here as part of your starting point. Remember, that code
# calculates weekly gross pay. Extend that calculation to estimate annual gross pay
# (how many weeks in a year?) and save it to a new variable.
# -----------------------------------------------------------------------------------------------

# Single Filers
# Annual Income Range       Tax Rate
# Under 12000               5 %
# 12000 - 24999.99          10 %
# 25000 - 74999.99          15 %
# 75000 and over            20 %

# Joint Filers
# Annual Income Range       Tax Rate
# Under 12000               0 %
# 12000 - 24999.99          6 %
# 25000 - 74999.99          11 %
# 75000 and over            20 % 
# -------------------------------------------------------------------------------------------------

pay_rate = eval(input("Please enter your pay rate.: "))
hours_worked = eval(input(" Please enter how many hours you wokred.: "))
filing_status = input("Enter filing status (single or joint): ").strip().lower()

if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay
else:
    gross_pay = hours_worked * pay_rate

annual_income = gross_pay * 52

if filing_status == "single":
    if annual_income < 12000:
        tax_rate = .05
    elif 12000 <= annual_income <= 24999.99:
        tax_rate = .10
    elif 25000 <= annual_income <= 74999.99:
        tax_rate = .15
    elif annual_income >= 75000:
        tax_rate = .20
    elif filing_status == "joint":
        if annual_income < 12000:
            tax_rate = 0
        elif 12000 <= annual_income <= 24999.99:
            tax_rate = .06
        elif 25000 <= annual_income <= 74999.99:
            tax_rate = .11
        elif annual_income >= 75000:
            tax_rate = .20
    else:
        print("Error! Please enter valid filing status: ")
        tax = 0

weekly_tax_withhold = gross_pay * tax_rate
net_pay = gross_pay - weekly_tax_withhold

print(f"You worked {hours_worked} this period.")
print(f"Because you earn ${pay_rate:.2f}per hour, your gross weekly pay is ${gross_pay:,.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is ${weekly_tax_withhold:,.2f}")
print(f"Your net pay is ${net_pay:,.2f}")

# ---- Output ----------
# Please enter your pay rate.: 12.50
# Please enter how many hours you wokred.: 40
# Enter filing status (single or joint): single
# You worked 40 this period.
# Because you earn $12.50per hour, your gross weekly pay is $500.00
# Your filing status is single
# Your tax withholding for the week is $75.00
# Your net pay is $425.00






















































