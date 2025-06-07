# Global scope: Define a variable in the global namespace
value = 100

def outer_function():
    # Enclosing scope: Redefine 'value' in the enclosing namespace
    value = 50
    
    def inner_function():
        # Local scope: Define 'value' in the local namespace
        value = 10
        # Print the local variable (LEGB: Python finds 'value' in the Local namespace)
        print(f"Inner function (local scope): {value}")
    
    # Call the inner function
    inner_function()
    # Print the enclosing variable (LEGB: Python finds 'value' in the Enclosing namespace)
    print(f"Outer function (enclosing scope): {value}")

# Call the outer function
outer_function()
# Print the global variable (LEGB: Python finds 'value' in the Global namespace)
print(f"Global scope: {value}")

# Comments explaining the LEGB rule:
# L (Local): Python first checks the local namespace (e.g., 'value' inside inner_function).
# E (Enclosing): If not found locally, it checks the enclosing namespace (e.g., 'value' in outer_function).
# G (Global): If not found in enclosing, it checks the global namespace (e.g., 'value' at the top).
# B (Built-in): Finally, it checks the built-in namespace (e.g., functions like 'print').
# In this script, each 'value' is resolved based on the closest namespace according to LEGB.
