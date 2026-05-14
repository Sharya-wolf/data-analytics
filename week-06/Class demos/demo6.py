# ========================================================================================
# Description: Class demos - For references
# Sha'Rya weaver
# 5/13/2026
# =========================================================================================
import random
# 1. random.randint(a, b) - Random integer between a and b
# (inclusive)
print("randint(1, 10):", random.randint(1, 10))

# 2. random.random() - Random float between 0.0 and 1.0
print("random():", random.random())

# 3. random.choice(seq) - Random single element from a sequence
fruits = ["apple", "banana", "cherry"]
print("choice(fruits):", random.choice(fruits))

# 4. random.choices(seq, k=n) - List of k random elements (with
# replacement))
print("choices(fruits, k=3):", random.choices(fruits, k=3))

# 5. random.sample(seq, k=n) - List of k unique random elements
# (without replacement)
# print("sample(fruits, k=2):" random.sample(fruits, k=2))

# 6. random.shuffle(seq) - Shuffles a list in place
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("shuffled numbers:", numbers)
# =====================================================================================================================
# DateTime
from datetime import date, time, datetime, timedelta, timezone

# date(year, month, day)
today = date(2026, 5, 9)
print("Date", today)

# time(hour, minute, second, microsecond)
current_time = time(14, 30, 45)
print("Time", current_time)

# datetime(year, month, day, hour, minute, second)
current_datetime = datetime(2026, 5, 9, 14, 30)
print("DateTime:", current_datetime)

# ---- Statistics ------
import statistics

# Sample dataset
data = [10, 20, 20, 40, 50]
print("=== Python Statistics Module Demo ===\n")

# mean() - average value
print("mean:", statistics.mean(data))

# median() - middle value
print("median:", statistics.median(data))

# mode() - most common value
print("mode:", statistics.mode(data))

#stdev() - standard deviation (sample)
print("stdev:", statistics.stdev(data))

# Variance() - variance (sample)
print("variance:", statistics.variance(data))

# Class Exercise 
# import statistics

# def analyst(name, region, sales):
    # return name, region, sales

# name, region, sales = analyst(
   # input("Please enter your name: "),
   # input("Please enter your region: "),
   # input("Please enter your seven daily sales figures: ")

# ---- Lambda dunctions --------
# contains any number of arguments but contains only one expression.

# Lambda functions to double a number
doubler = lambda n: n * 2

print(doubler(5))

# Lambda function to add a number
add_numbers = lambda a, b: a + b

print(add_numbers(3, 7))

# Lambda function to determine largest number
largest = lambda x, y: x if x > y else y

print(largest(12, 8))



