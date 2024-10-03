# Auto-Scheduler
A Python-based automation tool that converts scheduled tasks into a predefined format and generates reminders or task lists.

## Features
- Converts schedules from various formats into a unified structure.
- Generates reminders or customized task lists for easier management.

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
