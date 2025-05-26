# multiplication_table.py
# This script generates a multiplication table for numbers 1 to 10

# Generate and print the multiplication table
print("Multiplication Table for numbers 1 t0 10:\n")
for i in range(1, 11):  # outer loop for rows
    for j in range(1, 11):  # inner loop for columns
        product = i * j
        print(f"{i} * {j} = {product}")
    print("\n")
