# ===========================================================================================
# Description:
# Sha'Rya weaver
# Date: 5/10/2026
# ===========================================================================================

# 1. Create a script named show_major.py that defines two variables for a student:
# student_name and student_major. The student_major variable will contain a
# code for the student’s major (e.g. ENG).

# 2. Use the following table to create lookup logic to display the name of the major and
# location of the department’s office based on the major code:

# Major Code    Name of Major      Department Office
# ---------------------------------------------------
# BIOL          Biology            Science Bldg, Room 310
# CSCI          Computer Science   Sheppard Hall, Room 314
# ENG           English            Kerr Hall, Room 201
# HIST          History            Kerr Hall, Room 114
# MKT           Marketing          Westly Hall, Room 310
# ---------------------------------------------------

student_name = input('Please enter your name: ')
student_major = (input('Please enter your major code: ')).strip().upper()

if student_major == 'BIOL':
    major_name = 'Biology'
    location ='Science Bldg, Room 310'
elif student_major == 'CSCI':
    major_name = 'Computer Science'
    location = 'Sheppard Hall, Room 314'
elif student_major == 'ENG':
    major_name = 'English'
    location = 'Kerr Hall, Room 201'
elif student_major == 'HIST':
    major_name = 'History'
    location = 'Kerr Hall, Room 114'
elif student_major == 'MKT':
    major_name = 'Marketing'
    location = 'Westly Hall, Room 310'
else : 
    major_name = '<unknown>'
    location = 'No location found'

print(f'Student Name: {student_name}')
print(f'Major Code: {student_major}')
print(f'Major Name: {major_name}')
print(f'Department Office: {location}')

# ---- Output ----------------------------

# Please enter your name: Shawnette Tyson
# Please enter your major code: MKT
# Student Name: Shawnette Tyson
# Major Code: MKT
# Major Name: Marketing
# Department Office: Westly Hall, Room 310

# Please enter your name: Sha'Rya Weaver
# Please enter your major code: CSC
# Student Name: Sha'Rya Weaver
# Major Code: CSC
# Major Name: <unknown>
# Department Office: No location found










































