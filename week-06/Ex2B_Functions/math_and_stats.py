# ==========================================================================================
# description: Importing three modules
# Sha'Rya Weaver
# 5/14/2026
# ==========================================================================================
# Begin by importing three modules

import random
import math
import statistics

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi
# -------------------------------------------------------------------------------------------
# Use a combination of functions from all three modules to create calculations that will
# support the following output (and be sure to use comments to document your codeas you work!):

# _Experimenting with a subset of integers 1-100:
# Sum of 75 sample values from 1 to 100: ____
# Average of 75 sample values: ____
# Median of 75 sample values: ___

sum_sample = sum(vals_sample)   
# by using sum and then locking in the value vals_sample will then give the sum for it
avg_sample = statistics.mean(vals_sample) 
# We use the import statistics specifically statistics.mean to get the average
median_sample = statistics.median(vals_sample)
# Using the import statistics to clarify you put the type of statistics you want it to use after the word
# statistics
# ---- Output ---------------

print(
    f"_Experimenting with a Subset of Integers 1-100:\n"
    f"Sum of Random 75 Sample Values: {sum_sample}\n"
    f"Average of Random 75 Sample Values: {avg_sample}\n"
    f"Median of 75 Sample Values: {median_sample}"
)

# _Experimenting with a Subset of Integers 1-100:
# Sum of Random 75 Sample Values: 3644
# Average of Random 75 Sample Values: 48.586666666666666
# Median of 75 Sample Values: 47



























































