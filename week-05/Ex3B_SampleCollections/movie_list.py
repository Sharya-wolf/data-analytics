# ==============================================================
# Description: Focusing on making lists & descriptive statement
# Author: Sha'Rya Weaver
# Date: 5/9/2026
# ==============================================================

# Create a list with the titles of your favorite movies 
# (or movies you’d like to watch) – include at least 2, but no more than 10.
movies = ["Jester", "Scary Movie", "A Quiet Place"]

# Use the len() function to print the descriptive statement:
print(f"The list movies includes the {len(movies)} movies I want to watch.")
# Output: The list movies includes the 3 movies I want to watch.

print(movies)
# Output: ['Jester', 'Scary Movie', 'A Quiet Place']
# ========================================================================
# ---- Using Sorted ------------------------------------------------------
print(sorted(movies)) # Output: ['A Quiet Place', 'Jester', 'Scary Movie']
print(movies) # Output: ['Jester', 'Scary Movie', 'A Quiet Place']

# The difference between the two is when using sorted it put the list in 
# alphabetical listing. While without it the listing is just listed as you
# inputed. 
# ==========================================================================
# ---- Using Sort ----------------------------------------------------------
movies.sort() 
print(movies) # Output: ['A Quiet Place', 'Jester', 'Scary Movie']

# The difference between sort and sorted is that sort changes the list permenantly
# while sorted changes it temporarily but both orders your list alphabetically.
# ==========================================================================
# ---- Using append --------------------------------------------------------
movies.append("Now You See Me Now You Don't")

print(f"The list movies now include {len(movies)} movies I want to watch")
print(movies)

# Output: The list movies now include 4 movies I want to watch.
# Output: ['A Quiet Place', 'Jester', 'Scary Movie', "Now You See Me Now You Don't"]

# The append function adds to the list. Hvaing the sort permenant the list is 
# placed in alphabetical order except the newly added movie. In order to get it all
# in alphabetical order you would need to use sort again.











