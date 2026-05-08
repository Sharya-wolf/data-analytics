# Sha'Rya Weaver
# 5/7/2026

Celsius = float(input("Enter temperature in Celsius: "))  # can also use eval instead of float

# Convert to Fahrenheit
Fahrenheit = (9/5) * Celsius + 32

print(f"Fahrenheit = {Fahrenheit:.2f}")

# Sample Python tuple

student = ("Alice", 20, "Data Analytics", 3.5, True)

print(student)
print(f"Name    : {student[0]}")
print(f"Age     : {student[1]}")
print(f"Major   : {student[2]}")
print(f"GPA     : {student[3]}")
print(f"Active  : {student[4]}")
print(f"Length  : {len(student)}")

# Python tuple Functions

# count(x)
t = (1,2, 2, 3, 2)
print(t.count(2))  # Output: 3  Tells how many of that number is there

# index(x)
print(t.index(2))  # Output: 1 Telling the place it in or the index

# len(t)
print(len(t)) # Output: 5 Tells how many values is thre in a total

# min(t)
print(min(t))  

# max(t)
print(max(t))

# sum(t)
print(sum(t))  # Output: 10

# sorted(t)
print(sorted(t))

# type(t)
print(type(t))

# index
t = ("a", "b", "c")
print(t[0])
print(t[-1])

# slice

t = (1, 2, 3, 4, 5)
print(t[1:4])    # Output: (2,3,4)

# concatenation
t = (1, 2, 3)
t2 = ("a", "b", "c")
t3 = t + t2
print(t3)

# repitition
t = (1, 2, 3)
t2 = t * 3
print(t2)

# membership
t = (1, 2, 3)
print(2 in t)

# uniqueness
t = (1, 2, 3, 4, 5)
print(len(set(t)))

# convert to list
t = (1, 2, 3, 4, 5)
print(list(t))

States = ("Ohio", "Alaska", "Virginia", "Pennsylvania", "Mississippi")
print(f"Total number of states   :  {len(States)}")
print(f"First state   : {States[0]}")
print(f"Last state   :  {States[4]}")
print(f"Is Texas in ther tuple? {"Virginia" in States}")
print(f"States in alphabetical order: {sorted(States)}")
print(f"Longest State name length: {max(States)}")


# Python sets

# Iterate with a loop
my_set = {"Alice", "Bob", "Charlie"}

for item in my_set:
    print(item)

# Membership test with in
my_set = {1, 2, 3, 4, 5}

print(3 in my_set)
print(9 in my_set)

# Convert to a list - then access by index
my_set = {1, 2, 3, 4, 5}

my_list = list(my_set)
print(my_list[2])

# Convert to a sortedlist - access in a predictible order
my_set = {1, 2, 3, 4, 5}

my_list = sorted(my_set)
print(my_list[2])

# Unpacking - assign elements to variable (order not guarenteed)
my_set = {1, 2, 3, 4, 5}




# For loops
num = 5
if num > 5:
    print('Hello')
print("Done")    # only evaluates if true

if num > 5:
    print('Hello')
else:
    print('Hi')
print('Done')

num = int(input("Enter a number"))
if num > 0:
    print('Positive')
elif num < 5:
    print('Hi')
else:
    print('Hi')
print('Done')


# y loop
num = 5
while num > 0:
    print('Hello')
    num -=1


# for loop - user control
for item in [1, 2, 3, 4]:
    if item == 2:
        break
    print(item)


    if item == 2:
        continue
    print(item)


# Challenge
score = int(input("Enter score number: "))

if (score > 0 and score <= 100):
 if(score >= 90):
    print("Grade A")
elif(score >= 80):
    print("Grade B")
elif (score >= 70):
    print("Grade C")
elif(score >= 60):
    print("Grade D")
elif(score >=50):
    print("Grade E")
elif(score >= 40):
    print("Grade F")


