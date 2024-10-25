# Auto-Scheduler
A Python-based automation tool that generates timetables based on teacher and lab availability to design a proper timetable for each class smartly.

## Features
- Creates dynamic schedules from various use cases into a unified structure.
- Created a UI-interface for teachers and HODs to smartly manage schedules for both, students and teachers.

## Usage
### Install the required libraries:
```bash
pip install -r requirements.txt
```

### Run the code:
```bash
python ui.py
```

## Description of various files:
- **convert.py:** Converts input schedules into a standardized format (xlsx to csv).
- **generator.py:** Generates tasks or reminders based on the converted schedule, and is the core logic behind the programe.
- **icon.png:** Icon for the graphical interface.
- **requirements.txt:** Dependencies for running the project.
- **ui.py:** GUI interface for easier interaction with the scheduler.
