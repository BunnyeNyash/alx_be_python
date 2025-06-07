#  import the modules
from datetime import datetime, timedelta


def display_current_datetime():
    """Displays the current date and time in a formatted string.

    Retrieves the current date and time using the `datetime` module, stores it in
    `current_date`, and prints it in the format 'YYYY-MM-DD HH:MM:SS'.

    Args:
        None

    Returns:
        None

    Examples:
        >>> display_current_datetime()
        Current date and time: 2025-06-07 15:30:45
    """

    # save the current date and time in current_date
    current_date = datetime.now()
  
    # format and print the current date and time in 'YYYY-MM-DD HH:MM:SS'
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """Calculates and displays a future date by adding user-specified days to the current date.

    Prompts the user for a number of days, adds it to the current date using `timedelta`,
    stores the result in `future_date`, and prints it in the format 'YYYY-MM-DD'. Handles
    invalid input by prompting for a valid integer.

    Args:
        None

    Returns:
        None

    Examples:
        >>> calculate_future_date()
        Enter the number of days to add to the current date: 10
        Future date: 2025-06-17

    Raises:
        ValueError: If the user enters a non-integer value for the number of days.
    """

    # Get the current date
    current_date = datetime.now().date()
  
    # Prompt the user to enter a number of days (as an integer)
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        # Calculate the future date using timedelta
        delta = timedelta(days=number_of_days)
        future_date = current_date + delta
        # Print the future date in 'YYYY-MM-DD' format
        print(f"Future date: {future_date}")
    except ValueError:
        print("Invalid input. Please enter a valid integer (whole number).")

def main():
    """Runs the datetime exploration program by calling display_current_datetime and calculate_future_date."""
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
