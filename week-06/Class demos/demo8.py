# ==========================================================================================
# Description: Error Handling
# Sha'Rya Weaver
# Date: 5/15/2026
# ==========================================================================================
# Example of try, except, else, and finally in Python

try:
    # Ask the user for a number
    number = int(input("Enter a number: "))

    # Divide 100 by the number
    result = 100 / number

except ValueError:
    # Run if the user enters non-numeric data
    print("Error: Please enter a valid number.")

except ZeroDivisionError:
    # Runs if the user enters 0
    print("Error: Cannot divide by zero.")

else:
    # Runs only if no errors occur
    print(f"The result is: {result}")

finally:
    # Always runs whether an error occurs or not
    print("Program execution completed.")
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Error Handling

try:
    age = int(input("Enter your age: "))
    print("Next year you will be", age + 1)
except ValueError:
    print("That is not a valid age.")

while True:
    try:
        number = int(input("Enter a positive number: "))
        if number > 0:
            break
        else:
            print("Number must be positive.")
    except: 
        print("This is not a positive number.")








































































