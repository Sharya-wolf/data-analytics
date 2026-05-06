# Sha'Rya Weaver
# 5/6/2026
# Average

name = "Sha'Rya"
num1 = 15
num2 = 25
num3 = 5
average = (num1 + num2 + num3 / 3)
print(f'Hello {name}! The average of {num1}, {num2}, and {num3} is {average}')

# Ask the user to find the average of three numbers
name = input("Enter your name: ")
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
num3 = eval(input("Enter the third number: "))

print(f'The average of (num1),(num2) and (num3) is {(num1+num2+num3)/3:.2f}')

num4 = 10
print(type(num2))
print(type(str(num4)))

num5 = '25'
print(type(num5))
print(type(int(num5)))

print(type(float(num5)))
print(float(num5))

num6 = 3.14569
print(round(num6,2))

Original_price = input("Enter original price")
Discount = input("Enter discount percentage")

discount_amount = Original_price * (Discount / 100)
final_price = Original_price - discount_amount
print(f'The final price = ${final_price:.2f}')

# alignment with format specifier

January = 12345
February = 28123.678
March = 3112323.8976
April = 301234.678

print(f"{'January':<15}{January:>15,.2f}")
print(f"{'February':<15}{February:>15,.2f}")
print(f"{'March':<15}{March:>15,.2f}")
print(f"{'April':<15}{April:>15,.2f}")

# Class Exercise

Meal_cost = input("Enter meal cost ")

Meal_tip = Meal_cost * 0.20
Meal_tax = Meal_cost * 0.0825
Total = Meal_cost + Meal_tip + Meal_tax

print(f"{'Meal_cost':<6}{Meal_cost:>6,.2f}")


