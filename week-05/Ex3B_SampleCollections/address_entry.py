# =================================================================================
# Description: Define a dictionary named contact_info
# Author: Sha'Rya Weaver
# Date: 5/9/2026
# =================================================================================
# includes the following keys and the sample values of your choice:
# name, address, city, state, zip

contact_info = {
    "name": "Shawnette Tyson",
    "address" : "115 West 138th St",
    "city" : "New York",
    "state" : "New York",
    "zip" : "10030"
}

print(f"""Name: {contact_info["name"]}  
Address: {contact_info["address"]}       
City: {contact_info["city"]}            
State: {contact_info["state"]}          
Zip: {contact_info ["zip"]}""")         
#---- Output ----------------------------------------------------------------------
#  Name: Shawnette Tyson
# Address: 115 West 138th St
# City: New York
# State: New York
# Zip: 10030
# ---- Remove key:value for name -----------------------------------------------------------
del contact_info["name"]
print(contact_info)
# output: {'address': '115 West 138th St', 'city': 'New York', 'state': 'New York', 'zip': '10030'}
# ---- Adding full_name ---------------------------------------------------------------------
full_name = { "First name": "Shawnette",
             "Last name": "Tyson"}

# ---- Using .update() ----------------------------------------------------------------------
full_name.update({"honorific": "Ms."})
print(full_name)
# Output: {'First name': 'Shawnette', 'Last name': 'Tyson', 'honorific': 'Ms.'}

contact_info.update(full_name)
print(contact_info)
# Output: {'address': '115 West 138th St', 'city': 'New York', 'state': 'New York', 'zip': '10030', 
# 'First name': 'Shawnette', 'Last name': 'Tyson', 'honorific': 'Ms.'}

# ---- Formatted ------
print(f"""{contact_info["honorific"]} {contact_info["First name"]} {contact_info["Last name"]}
Address: {contact_info["address"]}
City: {contact_info["city"]}
State: {contact_info["state"]}
Zip: {contact_info["zip"]}""")

# Output: Ms. Shawnette Tyson
#         Address: 115 West 138th St
#         City: New York
#         State: New York
#         Zip: 10030


