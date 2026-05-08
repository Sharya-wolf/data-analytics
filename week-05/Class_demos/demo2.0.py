# Sha'Rya Weaver
# 5/5/2026 

name = "Hello"
print (f"Original string : {name}")

name1 = "Chantel Lee"
name2 = "Dimitri Nji"
name3 = "Vesna Cari"
print(f'The names of my three classmates are:\n {name1}, \n {name2}, \n {name3},')


# Accessing Characters - Used to accessed string using index and slicing
string = "Hello, World"

# Accessing the first  character
print(string[0])  # Output: H

# Accessing the last character
print(string[-1])   # Output: !

# Slicing from index 1 to 4 (excluding 4)
print(string[1:4])  # Output: ell


# String Operations - Conatenation( joining two or more strings using the pluse operator)
greeting = "Hello, " + "World!"
print(greeting)  # Output: Hello, World!

# Repetition - Repeating a string using * operator
repeat = "Hello! " * 3
print(repeat)  # Output: Hello! Hello! Hello!

# Membership - Checking if a submitting exists within a string using the 'in' keyword
print("World" in greeting)  # Output: True

# String Methods - Python provides metods for various operations such as converting case, finding substrings, replacing
string = "Hello, World!"

# Convert to uppercase
print(string.upper())  # Ouput: HELLO, WORLD!

# Find a substring
print(string.find("World")) # Output 7

# Replace a substring
print(string.replace("World", "Python"))  # Output: Hello, Python!

# Split a string
print(string.split(","))  # Output: ['Hello', 'World!']

# user input in python 

name = input("Sha'Rya Weaver: ")
print (f"Hello {name}")

# Ask the user to enter two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

print (f'You have entered {num1} and {num2}')

print(type(num1))
print(type(num2))

print(f'The sum of {num1} and {num2} is {num1+num2}')
print(f' The product of {num1} and {num2} is {num1*num2}')
print(f' The product of 2 and {num2} is {2*num2}')
