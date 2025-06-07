# variable in the global scope
message = "Hello from global scope!"

def print_message():
    # variable with the same name in the local scope
    message = "Hello from local scope!"
    # Print the local variable (Python uses the local namespace)
    print(f"Inside function: {message}")

# Call the function to print the local variable
print_message()
# Print the global variable (Python uses the global namespace)
print(f"Outside function: {message}")
