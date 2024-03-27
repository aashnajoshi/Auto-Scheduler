from tt_struct import create_timetable
import random

# Function to generate timetable for classes
def generate_class_timetable(classes_data):
    class_tt = {cls: [] for cls in classes_data}
    
    # Time slots available for classes
    class_time_slots = [(day, period) for day in range(1, 6) for period in range(1, 8)]

    # Iterate through each class
    for cls, cls_subjects in classes_data.items():
        for cls_subject in cls_subjects:
            # Randomly select a time slot for the class subject
            if class_time_slots:
                day, period = random.choice(class_time_slots)
                class_tt[cls].append((day, period, cls_subject))
                class_time_slots.remove((day, period))
            else:
                print("No available time slots for class:", cls)

    # Create and save timetable
    for cls, timetable in class_tt.items():
        create_timetable(f"{cls}_ClassTimeTable", timetable)

# Main entry point for class timetable generation
if __name__ == "__main__":
    # Example usage
    classes_data = {
        'aiml': ['sub1', 'sub2', 'sub3'],
        'cse': ['sub1', 'sub2', 'sub3'],
        'ece': ['sub1', 'sub2', 'sub3']
        # Define your classes data here
    }
    generate_class_timetable(classes_data)