# Ask the user for their task
task = input("Enter your task: ")

# Ask for priority level
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Give a message based on the priority using match-case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Add extra note if the task is time-bound
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority != "high":  # only add this if it's not high and not time-bound
        message += ". Consider completing it when you have free time."

# Print the final reminder
print()
print(message)
