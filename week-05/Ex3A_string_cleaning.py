# ============================================================
# Description: This script shows how to
#              clean a string.
# Author: Sha'Rya Weaver
# Date: 5/8/2026
# =============================================================
# Script:
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"
# =============================================================
# Cleaning
# ---- Lowering -----------------------------------------------
print(name_1.lower()) # Output: priya sharma
print(name_2.lower()) # Output: bob nguyen
print(name_3.lower()) # Output: latonya williams
# =============================================================
# ---- Title Case ---------------------------------------------
print(name_1.title()) # Output: Priya Sharma
print(name_2.title()) # Output: Bob Nguyen
print(name_3.title()) # Output: Latonya Williams
# =============================================================
# ---- Replacing ----------------------------------------------
print(salary_1.replace("$", "")) # Output: 82,500
print(salary_2.replace("$", "")) # Output: 74,000

# These are still strings because they have yet to be converted 
# into integers or float.

# In order to change them into int you will need to replace the 
# comma as well or use int() to convert into a integer.
# =============================================================
# ---- Usuable Integer ----------------------------------------
salary1_clean = int(salary_1.replace("$", "").replace(",", ""))

print(salary1_clean, type(salary1_clean)) # Output: 82500 <class 'int'>

