# ==============================================================================================
# Description: Class demos & Examples
# Sha'Rya Weaver
# Date: 5/14/2026
# ===============================================================================================

print()
# Create a class named student
class Student:


   # Constructor method with default values
   def _init_(self, name="Unknown", grade=0):
      self.name = name
      self.grade = grade

    # Method to display student information
def display_info(self):
  print(f"Student Name: (self.name)")
  print(f"Grade: (self.grade)")
  print("-----------------------")

# Create 2 student objects
student1 = Student("Alice", 95)

# Uses default grade value
student2 = Student("Brian")

# Display the student objects using f-strings
print(f"Student 1: {student1.name} -  {student1.grade}")
print(f"Student 2: {student2.name} - {student2.grade}")

print()

# Call the method for each student
student1.display_info()
student2.display_info()
# ------------------------------------------------------------------
# Define a Python class with class attributes

print()
# Create a call named Student
class Student:
   
   # Class attribute
   school = "Year Up United"   # When the class all go to the same school

   # constructor method
   def _init_(self, name, grade):
      # Instance attributes
      self.name = name
      self.grade = grade

    # Method to display student information
      def display_info(self):
       print(f"School: {Student.school}") 
       print(f"Student Name: {self.name}")
       print(f"Grade: {self.grade}")
       print("-------------------------------")


# Create 2 student objects
student1 = Student("Alice", 95)
student2 = Student("Brian", 88)

# Display student information
student1.display_info()
student2.display_info()
# -------------------------------------------------------------------------
















































