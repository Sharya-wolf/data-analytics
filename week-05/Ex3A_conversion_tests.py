#
# Sha'Rya Weaver
# 5/8/2026
#
# Description: This sript tests various numeric
#              conversion techniques
# Author: Sha'Rya W. Newprogrammer

# Variables
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '
# The quotation marks signal that these are strings

# New Variables
# 5a) Cast as integer using int()
# int(a) # This comes out as an error because as the terminal states 
       # it is and invalid literal for int() with base 10: ' 101.1'. 
       # This means that the number must be a whole number to be able to use the int function.

int(b) # Output: 55

# int(c) # ValueError: Invalid literal for int() with base 10: '402 Stevens'. It uses letters

# int(d) # ValueError: Invalid literal for int() with base 10: 'Number 5'. This also uses letters.

# 5b) Cast as float using float()
print(float(a)) # Just running this will give you 101.1. No errors. Why? 
         # Because the value of a is a decimal meaning it is a float.

print(float(b)) # Output: 55.0

# print(float(c)) # ValueError: could not convert string to float: '402 Stevens'. A float deals with only numbers.

# print(float(d))  # ValueError: could not convert string to float: 'Number 5'

# 5d) For variable a, try casting into a float then integer, like this: int(float(a))
print(int(float(a))) # This works giving the output 101 because you are first stating the vaules 
 # Output: 101       # data type before then changing it's data type into a integer. This causes the variable to
                     # change it's value to fit as a integer or whole number. Hint: There is no longer a decimal.

print(int(float(b))) # Output: 55

# print(int(float(c))) # ValueError: Could not convert string to float: '402 Stevens'

# print(int(float(d))) # VlaueError: Could not convert string to float: 'Number 5'

# 5d) Using slicing to add just the numeric portion of the string to a new variable(remember, indexing
      # alaways starts with 0!), and cast the number as an integer or string, whichever is appropiate.
sliced_a = float(a[2:7])
print(sliced_a, type(sliced_a)) # Output: 1.1 <class 'float'>

sliced_b = int(b[0:2])
print(sliced_b, type(sliced_b)) # Output: 55 <class 'str'>

sliced_c = str(c[0:3])
print(sliced_c, type(sliced_c)) # Output: 402 <class 'str'>

sliced_d = str(d[7:9])
print(sliced_d, type(sliced_d)) # Output: 5 <class 'str'>

# 5e) For variables a and d, use the .strip() method to remove the leading/trailing
    # spaces, within a print statement to display each result.
print(a.strip()) # Output: 101.1

print(d.strip()) # Output: Number 5


