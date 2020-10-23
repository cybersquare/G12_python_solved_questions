# Create a binary file with roll number, name and marks. Input a roll
# number and update the marks.  

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
roll_no = input('Please enter roll number update mark: ')
new_mark = input('Please enter mark: ')
flag = 0

# Search 
for stud in studList:
    if int(roll_no) == int(stud['rollno']):
        print('Name: ',stud['name'], '\nMarks: ', stud['marks'])
        stud['marks'] = new_mark
        flag = 1
if flag == 0:
    print('Student with roll number %s not found'%(roll_no))
else:
    # Save data to file
    with open('student.txt', 'wb') as f:
    # dumb method is used for serializind data and write to file
        pickle.dump(studList, f)

# Read data from file to see whether it got updated
pickle_off = open ("student.txt", "rb")
# load method is used to read from file and de-serializing it
studList1 = pickle.load(pickle_off)
print(studList1)
pickle_off.close()



