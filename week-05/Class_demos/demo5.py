# ============================================================
# Sha'Rya Weaver
# 5/12/2026
# ============================================================
# Define a function with no parameters

def greeting():
    name = input("Please enter your name: ")
    print(f"Hello, {name}!")

greeting()
# =============================================================
# demonstrates a return statement

def greeting():
    name = input("Please enter your name: ")
    return name

result = greeting()
print(f"Hello, {result}!")

# Python automatically packages multiple return values into a tuple

def greeting(name, city, hobby):
    return name, city, hobby

result = greeting(
    input("Please enter your name: "),
    input("Please enter your city: "),
    input("Please enter your hobby: ")
)

print(type(result))

print(f"Hello, {result[0]}! Your are from {result[1]} and you enjoy {result[2]}.")




