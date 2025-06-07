def display_menu():
    """Displays the menu options for the shopping list manager.

    Args:
        None

    Returns:
        None
    """
  
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Manages a shopping list that allows users to add, remove, and view items.

    Creates an empty list `shopping_list` and provides a loop to display a menu with options
    to add an item, remove an item, view the list, or exit. Handles user input for adding and
    removing items, including validation for invalid choices and items not in the list.

    Args:
        None

    Returns:
        None

    Examples:
        Sample interaction:
        Shopping List Manager
        1. Add Item
        2. Remove Item
        3. View List
        4. Exit
        Enter your choice: 1
        Enter item to add: Apples
        Apples added to the list!

    Notes:
        - The `shopping_list` is a global list maintained within the function.
        - Invalid menu choices prompt an error message and continue the loop.
        - Removing an item not in the list displays a message indicating the item was not found.
    """
  
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ").strip().capitalize()
            if item:  # Check if item is not empty
                shopping_list.append(item)
                print(f"{item} added to the list!")
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ").strip().capitalize()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the list!")
            else:
                print(f"{item} not found in the list.")
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("Current shopping list:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is empty.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
