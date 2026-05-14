#
# Description: Using Class 
# Sha'Rya Weaver
# Date: 5/13/2026
# 
class Product:
     # Constructor Method
     def _init_(self, name, category, price, quantity):
             self.name = name
             self.category = category
             self.price = price
             self.quantity = quantity

     # Method to display
     def display_info(self):
          print(f"Product Name: {self.name}")
          print(f"Category: {self.category}")
          print(f"Product Price: {self.price:.2f}")
          print(f"Product Quantity: {self.quantity} units")
          print("-----------------------")

    # Method Calculate total inventory value
     def inventory_value(self):
           total = self.price * self.quantity
           print(f"Inventory value for {self.name} : ${total:.2f}")
           print("---------------------------")

# Created 2 product objects using user input
print("=== Enter Product 1 ===")
name1     =       input("Product name:  ")
category1 =       input("Category:      ")
price1    = float (input("Price $:      "))
quantity1 = int   (input("Quantity:     "))

print("\n=== Enter Product 2 ===")
name2     =        input("Product name:   ")
category2 =        input("Category:       ")
price2    = float  (input("Price $:       "))
quantity2 = int    (input("Quantity:      "))
