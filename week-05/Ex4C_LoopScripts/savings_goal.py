#
# Description: More Loops!
# Sha'Rya Weaver
# 5/10/2026
# 
# Create a variable for your starting bank balance, another that sets your savings goal,
# and a third with your weekly savings amount

# Use a while loop to compare your bank balance to your savings goal, if you haven’t
# met your goal yet, add the weekly savings amount to your bank balance. For each loop,
# print the statement, “This week my balance increased to ___.” Once your savings goal
# is met, print the statement, “Goal met! My current balance is ___.”

# Try adding additional logic to your loop:
# a) If your balance is more than halfway to your goal, print the message, “Almost there!
# This week my balance is up to ___.”
# b) If your balance is at least 75% of your goal, add a calculation to buy yourself a little
# treat. Print the message, “So close! After treating myself, my balance is up to ___.”

starting_balance = float(input('What is your current bank balance?: '))
savings_goal = float(input('What is your savings goal?: '))
weekly_savings = float(input('What is your weekly savings amount?: '))
treat = float(input('How much will treating yourself cost?: '))

while starting_balance < savings_goal:
    starting_balance += weekly_savings

if starting_balance >= savings_goal * 0.75:
        starting_balance -= treat
        print(f'So close! After treating myself, my balance is up to ${starting_balance:.2f}')

elif starting_balance >= savings_goal * 0.50:
        print(f'Almost there! This week my balance is up to ${starting_balance:.2f}')

else:
        print(f'This week my balance increased to ${starting_balance:.2f}')

print(f'Goal met! My current balance is ${starting_balance:.2f}')

# ---- Output ---------------------

# What is your current bank balance?: 136   
# What is your savings goal?: 1000
# What is your weekly savings amount?: 40
# How much will treating yourself cost?: 32
# So close! After treating myself, my balance is up to $984.00
# Goal met! My current balance is $984.00















































