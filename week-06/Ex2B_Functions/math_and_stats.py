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
# ---- Output ---------------
# _Experimenting with a Subset of Integers 1-100:
# Sum of Random 75 Sample Values: 3644
# Average of Random 75 Sample Values: 48.586666666666666
# Median of 75 Sample Values: 47

# ----------------------------------------------------------------------------------------------------
# _Experimenting with a superset of 200 values, integers 1-100:
# Average of 200 values: ____
# Median of 200 values: ____
# Mode of 200 values: ____
# Standard deviation of 200 values: ____
# Variance of 200 values: ____

Ave_value = statistics.mean(vals_choices)
Med_value = statistics.median(vals_choices)
Mod_value = statistics.mode(vals_choices)
Dev_value = statistics.stdev(vals_choices)
Var_value = statistics.variance(vals_choices)
# For each of these we can use the statistics function to get the average, median, mode,
# standard deviation and variance.

print(
    f"Average of 200 values: {Ave_value}\n"
    f"Median of 200 values: {Med_value}\n"
    f"Mode of 200 values: {Mod_value}\n"
    f"Standard deviation of 200 values: {Dev_value}\n"
    f"Variance of 200 values: {Var_value}"
)
# ---- Output -----------------------
# Average of 200 values: 52.035
# Median of 200 values: 53.5
# Mode of 200 values: 77
# Standard deviation of 200 values: 28.99824591818716
# Variance of 200 values: 840.8982663316583

# --------------------------------------------------------------------------------------------------
# _Modeling a random circle:
# Radius = __, area = ____ (rounded up to the nearest integer)
# Radius = __, area = ____ (rounded down to the nearest integer)

circle_area = (pi * radius ** 2)
rounded_up = math.ceil(circle_area)
# .ceil rounds it up
rounded_down = math.floor(circle_area)
# using .floor rounds it down

print(f"_Modeling a random circle:\n"
      f"Radius = {radius}, area = {rounded_up} (rounded up to the nearest integer)\n"
      f"Radius = {radius}, area = {rounded_down} (rounded down to the nearest integer)")

# ---- Output -----------
# _Modeling a random circle:
# Radius = 4, area = 51 (rounded up to the nearest integer)
# Radius = 4, area = 50 (rounded down to the nearest integer)






































