# daily_reminder.py
# This script will ask the user for a single task, its priority level, and if it is time-sensitive. The program will
# then provide a customized reminder for that task, demonstrating control flow and loops
# without relying on data structures to store multiple tasks.
# Objective: Create a simplified Python script that uses conditional statements, Match Case, and loops
# to remind the user about a single, priority task for the day based on time sensitivity.

while True:
    # Prompt for a Single Task
    task = input("Enter your task: ").strip().capitalize()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    if priority in {"high", "medium", "low"} and time_bound in {"yes", "no"}:
        break
    else:
        print("Invalid input. Please try again with values (high, medium, low, yes, no) only.\n")

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task. You can complete it when you have time.")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be addressed soon.")
        else:
            print(f"Note: '{task}' is a medium priority task. Consider completing it when you can.")

    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that can be done at your convenience.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

    case _:
        # This should never happen due to input validation
        print("Invalid priority level. Please enter high, medium, or low.")
