# ===================================================
# Description: How to create files in Python
# Sha'Rya Weaver
# Date: 5/14/2026
# ====================================================
# Use the open () with one of the following options: 
# "x" "w" -to create a new file:

# X will creat a file only if there is no file already in existence with that name

# creating a text file with the command function "x"
f = open("myfile.txt", "x")

# w create a text file whether or not there is a file in the memory with new specified
# name. It will not give an error just overwrite it.

# creating a text file with command function "w"
f = open("myfile.txt", "w")

# The Write Method
# This function inserts the string into the text file on a single line.

file.write("Hello There\n")

# The writelines()


f.writelines(["Hello World ", "You are welcome to Fcc\n"])





















