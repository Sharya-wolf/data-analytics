# ======================================================
# Description: Practicing If scripts basics
# Author: Sha'Rya Weaver
# Date: 5/10/2026
# ======================================================
# Create two starting variable:
x = 100
y = 20
# 3a) If x divided by y is 5, print “x divided by y is 5” and set the value of x to 1 – otherwise
#     print “are the variables set up correctly?”
if x / y == 5:
    print("x divided by y is 5")
    x = 1
else:
    print("Are the variables set up correctly?")
# Output: x divided by y is 5
# ----------------------------------------------------------------------------------------------------------
# 3b) If x times y is y, print “now x times y is y” and then set x to 10 – otherwise print
# “Whoops, x equals” + the value of x
if x * y == y:
    print("now x times y is y")
    x = 10
else:
    print("whoops, x equals {x}")
# Output: now x times y is y
# ----------------------------------------------------------------------------------------------------------
# 3c) If x is less than y, print “x is less than y” and double the value of x – otherwise print
# “uh oh, x is not less than y”
if x < y:
    print("x is less than y")
    x = x * 2
else:
    print("uh oh, x is not less than y")
# Output: x is less than y
# -------------------------------------------------------------------------------------------------------------
# 3d) If x is greater than y, print “how is x greater than y??” otherwise print “x is NOT
# greater than y”
if x > y:
    print("how is x greater than y??")
else:
    print("x is NOT greater than y")
# Output: x is NOT greater than y
# --------------------------------------------------------------------------------------------------------------
# 3e) Add a final print statement to say “The final value of x is __ and the final value of y
# is __” (displaying the actual values in place of the blanks)

print("The final value of x is {x} and the final value of y is {y}.")
# Output: The final value of x is {x} and the final value of y is {y}.



