import os
from generator import *

os.system('cls')
 
data={'Teachers': [{'Name': 'teacher1'}, {'Name': 'teacher2'}, {'Name': 'teacher3'}, {'Name': 'teacher4'}, {'Name': 'teacher5'}], 
 'Classes': [{'Name': 'aiml', 'Subjects': 'sub1,sub2,sub3,sub4', 'Lab Subjects': 'lab_sub3,lab_sub2'}, {'Name': 'cse', 'Subjects': 'sub1,sub2,sub4,sub5', 'Lab Subjects': 'lab_sub2,lab_sub5'}, {'Name': 'ece', 'Subjects': 'sub1,sub5,sub6', 'Lab Subjects': 'lab_sub1'}], 
 'Labs': [{'Name': 'lab1'}, {'Name': 'lab2'}, {'Name': 'lab3'}, {'Name': 'lab4'}], 
 'Relations': [{'Subject': 'sub1', 'Class': 'aiml', 'Name': 'teacher1', 'Lectures': '3'},
               {'Subject': 'sub1', 'Class': 'cse', 'Name': 'teacher1', 'Lectures': '3'},
               {'Subject': 'sub5', 'Class': 'ece', 'Name': 'teacher1', 'Lectures': '3'},
               {'Subject': 'sub2', 'Class': 'aiml', 'Name': 'teacher2', 'Lectures': '3'},
               {'Subject': 'sub2', 'Class': 'cse', 'Name': 'teacher2', 'Lectures': '2'},
               {'Subject': 'sub1', 'Class': 'ece', 'Name': 'teacher2', 'Lectures': '3'},
               {'Subject': 'lab_sub2', 'Class': 'aiml', 'Name': 'teacher2', 'Lectures': '1'},
               {'Subject': 'lab_sub2', 'Class': 'cse', 'Name': 'teacher2', 'Lectures': '1'},
               {'Subject': 'sub3', 'Class': 'aiml', 'Name': 'teacher3', 'Lectures': '2'},
               {'Subject': 'lab_sub3', 'Class': 'aiml', 'Name': 'teacher3', 'Lectures': '1'},
               {'Subject': 'lab_sub1', 'Class': 'ece', 'Name': 'teacher3', 'Lectures': '1'},
               {'Subject': 'sub4', 'Class': 'aiml', 'Name': 'teacher4', 'Lectures': '4'},
               {'Subject': 'sub4', 'Class': 'cse', 'Name': 'teacher4', 'Lectures': '2'},
               {'Subject': 'sub5', 'Class': 'cse', 'Name': 'teacher5', 'Lectures': '4'},
               {'Subject': 'sub6', 'Class': 'ece', 'Name': 'teacher5', 'Lectures': '3'},
               {'Subject': 'lab_sub5', 'Class': 'cse', 'Name': 'teacher5', 'Lectures': '1'},]}
initialize(data)

T_T_G(classes.keys())
print(classes)
for cls in classes.keys():
    print(cls)
    for r in ctt[cls]:
        print(r)
for cls in teachers.keys():
    print(cls)
    for r in ttt[cls]:
        print(r)