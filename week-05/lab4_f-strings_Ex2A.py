# -------------------------------------
# Sha'Rya Weaver
# 5/8/2026
# Modified tip amount using f-string
# ------------------------------------

# Script: 
Bill = 75.89
Tip_percent = .30 # 30%

# Calculations
Tip = Bill * Tip_percent

# Results
print(f"The tip on a ${Bill} restaurnant bill is ${Tip:.2f}")

# Output:  The tip on a $75.89 resturant bill is $22.77

# Observation
# Using the f-string makes your work clearer whne the output commes. I think of it as putting the variables into sentences. 
# This makes the output more readable and understanding. Instead of just saying the bill is 75.89 and then writing another 
# string saying the tip percent is .30, you can combine both to make one sentence.


