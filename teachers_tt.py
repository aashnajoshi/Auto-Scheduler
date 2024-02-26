from tt_struct import create_timetable, tt_structure

def get_initial_info():
    num_of_teachers = int(input("Enter No. of Teachers: "))
    teachers = {}
    for i in range(num_of_teachers):
        name = input(f"Teacher {i+1} Name: ").capitalize()
        num_of_subjects = int(input(f"Number of Subjects taught by {name}: "))
        subjects = [input(f"Subject {j+1} for {name}: ") for j in range(num_of_subjects)]
        teachers[name] = subjects
    return teachers

teachers_info = get_initial_info()

create_timetable(teachers_info,tt_structure)