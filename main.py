from openpyxl import Workbook

def get_initial_info():
    num_of_teachers = int(input("Enter No. of Teachers: "))
    teachers = {}
    for i in range(num_of_teachers):
        name = input(f"Teacher {i+1} Name: ").capitalize()
        num_of_subjects = int(input(f"Number of Subjects taught by {name}: "))
        subjects = [input(f"Subject {j+1} for {name}: ") for j in range(num_of_subjects)]
        teachers[name] = subjects
    return teachers

def create_teacher_timetable(teacher_name, subjects, tt_structure):
    wb = Workbook()
    ws = wb.active
    for row in tt_structure:
        ws.append(row)

    wb.save(f"{teacher_name}_TimeTable.xlsx")
    print(f"{teacher_name}_TimeTable.xlsx created!")

def create_class_xls():
    print("class working")

tt_structure = [["", "1st", "2nd", "3rd", "4th","", "5th", "6th", "7th"], ["Mon"], ["Tues"], ["Wed"], ["Thurs"], ["Fri"]]

teachers_info = get_initial_info()

for teacher, subjects in teachers_info.items():
    create_teacher_timetable(teacher, subjects, tt_structure)
# create_class_xls()