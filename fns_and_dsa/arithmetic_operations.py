def perform_operation(num1, num2, operation):
    """Performs a basic arithmetic operation on two numbers based on the specified operation.

    Args:
        num1 (float): The first number for the arithmetic operation.
        num2 (float): The second number for the arithmetic operation.
        operation (str): The operation to perform. Must be one of 'add', 'subtract',
                         'multiply', or 'divide'.

    Returns:
        float or str: The result of the arithmetic operation as a float, or a string
                      message 'Cannot divide by zero' if division by zero is attempted.

    Examples:
        >>> perform_operation(5.0, 6.0, 'add')
        11.0
        >>> perform_operation(5.0, 0.0, 'divide')
        'Cannot divide by zero'

    Raises:
        ValueError: If the operation is not one of 'add', 'subtract', 'multiply', or 'divide'.
    """

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return 'Cannot divide by zero'
        return num1 / num2
    else:
        raise ValueError("Operation must be one of 'add', 'subtract', 'multiply', or 'divide'")
