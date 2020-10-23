# 1. Create a binary file with name and roll number. Search for a given roll
# number and display the name, if not found display appropriate message. 

import pickle

n = int(input('Enter number of students: '))
students = list()

# Get data from user
for i in range(n):
    student = dict()
    name = input('Enter name of student: ')
    student['name'] = name
    rollno = input('Enter rollno: ')
    student['rollno'] = rollno
    marks = input('Enter marks: ')
    student['marks'] = marks
    students.append(student)

# Save data to file
with open('student.txt', 'wb') as f:
  # dumb method is used for serializind data and write to file
  pickle.dump(students, f)


# Read data from file
pickle_off = open ("student.txt", "rb")
# load method is used to read from file and de-serializing it
studList = pickle.load(pickle_off)
pickle_off.close()

# Get roll no
roll_no = input('Please enter roll number to search: ')
flag = 0

# Search 
for stud in studList:
    if int(roll_no) == int(stud['rollno']):
        print('Name: ',stud['name'], '\nMarks: ', stud['marks'])
        flag = 1
if flag == 0:
    print('Student with roll number %s not found'%(roll_no))





