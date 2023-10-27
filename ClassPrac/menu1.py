student = {}

print('Enter student details') 
while True:
    roll_number = int(input('Enter your 6 digit roll number: '))
    if roll_number in student:
        print('Roll Number Already Exists')
    else:
        name = input('Enter name: ')
        student[roll_number] = name
        print('Record added')
    ans = input('Do you want to continue(y/n)? ')
    if ans in 'nN':
        break

#######################################################
# a) Display the Roll numbers and name for all students
#######################################################

print('\nRoll Number','Name')
for roll_number in student:
    print(roll_number,'\t\t',student[roll_number])

#############################################################
# b) Add a new key-value pair in this dictionary and display 
#############################################################

print('\nEnter a new record ')
roll_number = int(input('Enter your 6 digit roll number: '))
if roll_number in student:
    print('Roll Number Already Exists')
else:
    name = input('Enter name: ')
    student[roll_number] = name
    print('Record added\n')

for roll_number in student:
    print(roll_number,'\t',student[roll_number])
    
#############################################################
# c) Delete a particular student's record from the dictionary
#############################################################

print('\nDelete a record ')
roll_number = int(input('Enter roll number: '))
if roll_number in student:
    del student[roll_number]
    print('Record deleted')
else:
    print('Record not found')

#############################################
# d) Modify the name of an existing students.
#############################################

print('\nModify a record')
roll_number = int(input('Enter new 6 digit roll number: '))

if roll_number in student:
    name=input('Modify name ')
    student[roll_number] = name
    print('Record updated')
else:
    print('Record not found')