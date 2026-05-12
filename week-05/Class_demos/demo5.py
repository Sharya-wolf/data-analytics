# ============================================================
# Sha'Rya Weaver
# 5/12/2026
# ============================================================
# Define a function with no parameters

def greeting():
    name = input("Please enter your name: ")
    # print(f"Hello, {name}!")

greeting()
# =============================================================
# demonstrates a return statement

def greeting():
    name = input("Please enter your name: ")
    return name

result = greeting()
# print(f"Hello, {result}!")
# ================================================================
# Python automatically packages multiple return values into a tuple

def greeting(name, city, hobby):    # Parameters
    return name, city, hobby

result = greeting(
    input("Please enter your name: "),
    input("Please enter your city: "),
    input("Please enter your hobby: ")
)                           # Arguments

# print(type(result))       

# print(f"Hello, {result[0]}! Your are from {result[1]} and you enjoy {result[2]}.")
#
# unpack as variables

def greeting(name, city, hobby):
    return name, city, hobby

name, city, hobby = greeting(
    input("Please enter your name: "),
    input("Please enter your city: "),
    input("Please enter your hobby: ")
)

# print(f"Hello, {name}! You are from {city} and you enjoy {hobby}.")

# Use a default parameter city = New York

def greeting(name, city, hobby):
    return f"Hello, {name}! You are from {city} and you enjoy\
    {hobby}." 

result = greeting(
    input("Please enter your name: "),
    input("Please enter your city: "),
    input("Please enter your hobby: ")
)

# print(result)

# Use a default parameter city = New York

def greeting(name, hobby, city = "New York"):
    return f"Hello, {name}! You are from {city} and you enjoy\
    {hobby}."

result = greeting(
    name = input("Please enter your name: "),
    hobby = input("Please enter your hobby: ")
)

# print(result)






# Class Execise
def movie(name, movie_name):
    return f"Hello, {name}! Your favorite movie is {movie_name}."

result = movie(
    name = input ("Please enter your name: "),
    movie = input ("Please enter your favorite movie: ")

)

# print(result)

# Demonstrating features of strings as a sequence in Python

# 1. Creating a string
text = "Python"

# 2. Indexing (positive and negative)
# print("First character:", text[0])
# print("Last character:", text[-1])


full_name = ["Sha'Rya Weaver", "Shawnette Tyson"]

def part_name(full_name):
    part = full_name.split(" ")
    first_name = part[0]
    last_name = part[-1]
    return first_name, last_name

first, last = part_name

print(f"First Name: {first}")
print(f"Last Name: {last}")


