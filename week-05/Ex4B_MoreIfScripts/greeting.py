# =================================================================================================
# Description: Using if/elif/else for greetings
# sha'Rya Weaver
# Date: 5/10/2026
# ==================================================================================================
# Define a variable that contains the current hour (0-
# 23). Display one of the greetings below based on the current hour:

# 2. Update your script to include an additional condition that will print “What are you
# doing up so late??” if the hour is between 11pm and 4am.

#    Time                    Greeting
# until 10:00am            Good morning!
# 10:00am until 5:00pm     Good day!
# 5:00pm or later          Good evening!


hour = eval(input("Please enter the time it is: "))

if hour < 10:
    print("Good morning!")
elif 10 <= hour < 17:
    print("Good day!")
elif hour >= 23 or hour < 4:
    print("What are you doing up so late?")
elif hour >= 17:
    print("Good evening!")
else:
    print("Wrong hour. Please eneter correct hour: ")

# Output: Please enter the time it is: 8 Good morning!
















































