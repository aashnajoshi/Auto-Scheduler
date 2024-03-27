# main.py

from class_tt import generate_class_timetable
from labs_tt import generate_lab_timetable
from teachers_tt import teachers_info
from tt_struct import create_timetable  # Importing create_timetable function from tt_struct

# Main function to generate the entire timetable
def generate_timetable():
    # Example data
    classes_data = {
        'aiml': ['sub1', 'sub2', 'sub3'],
        'cse': ['sub1', 'sub2', 'sub3'],
        'ece': ['sub1', 'sub2', 'sub3']
        # Define your classes data here
    }

    labs_data = {
        'lab1': ['lab_sub1', 'lab_sub2', 'lab_sub3'],
        'lab2': ['lab_sub4', 'lab_sub5']
        # Define your labs data here
    }

    # Call functions to generate class timetable, lab timetable, and teacher timetable
    generate_class_timetable(classes_data)
    generate_lab_timetable(labs_data)

    # Generate teacher timetable using the fetched teachers' information
    for name, subjects in teachers_info.items():
        create_timetable(name, [subjects])  # Wrap subjects in a list to ensure it's passed as a list

# Main entry point of the application
if __name__ == "__main__":
    generate_timetable()