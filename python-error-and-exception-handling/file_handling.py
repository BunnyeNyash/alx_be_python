try:
    filename = input("Enter the file name: ")
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to access '{filename}'.")
else:
    print("File contents:")
    print(content)
finally:
    print("File operation completed.")
