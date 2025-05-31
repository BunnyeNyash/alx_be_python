# daily_reminder.py
# This script will ask the user for a single task, its priority level, and if it is time-sensitive. The program will
# then provide a customized reminder for that task, demonstrating control flow and loops
# without relying on data structures to store multiple tasks.
# Objective: Create a simplified Python script that uses conditional statements, Match Case, and loops
# to remind the user about a single, priority task for the day based on time sensitivity.

# Prompt for a Single Task
task = input("Enter your task: ").strip().capitalize()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += ". You can complete it when you have time."

    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that should be addressed soon."
        else:
            reminder += ". Consider completing it when you can."

    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            reminder += " that can be done at your convenience."
        else:
            reminder += ". You can do it whenever you have free time."

    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

# Provide a Customized Reminder
print(reminder)
