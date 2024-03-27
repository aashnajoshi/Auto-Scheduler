from tt_struct import create_timetable
import random

# Function to generate timetable for labs
def generate_lab_timetable(labs_data):
    labs_tt = {lab: [] for lab in labs_data}
    
    # Time slots available for labs
    lab_time_slots = [(day, period) for day in range(1, 6) for period in range(1, 8)]

    # Iterate through each lab
    for lab, lab_subjects in labs_data.items():
        for lab_subject in lab_subjects:
            # Randomly select a time slot for the lab subject
            if lab_time_slots:
                day, period = random.choice(lab_time_slots)
                labs_tt[lab].append((day, period, lab_subject))
                lab_time_slots.remove((day, period))
            else:
                print("No available time slots for lab:", lab)

    # Create and save timetable
    for lab, timetable in labs_tt.items():
        create_timetable(f"{lab}_LabTimeTable", timetable)

# Main entry point for lab timetable generation
if __name__ == "__main__":
    # Example usage
    labs_data = {
        'lab1': ['lab_sub1', 'lab_sub2', 'lab_sub3'],
        'lab2': ['lab_sub4', 'lab_sub5']
        # Define your labs data here
    }
    generate_lab_timetable(labs_data)