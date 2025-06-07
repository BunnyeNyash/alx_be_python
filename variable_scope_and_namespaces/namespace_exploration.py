# Function 1: Counting function
def count_items():
    # Local variable 'count' in the local namespace of count_items
    count = 5
    print(f"Counting function: {count} items processed")

# Function 2: Logging function
def log_event():
    # Local variable 'count' in the local namespace of log_event
    count = 3
    print(f"Logging function: {count} events logged")

# Call both functions to demonstrate separate namespaces
count_items()
log_event()
