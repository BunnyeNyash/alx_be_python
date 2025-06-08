# Global Conversion Factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius using a global conversion factor.

    Uses the global `FAHRENHEIT_TO_CELSIUS_FACTOR` to perform the conversion.

    Args:
        fahrenheit (float): The temperature in Fahrenheit to convert.

    Returns:
        float: The temperature converted to Celsius.

    Examples:
        >>> convert_to_celsius(100.0)
        37.77777777777778
    """

    temperature = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temperature

def convert_to_fahrenheit(celsius):
    """Converts a temperature from Celsius to Fahrenheit using a global conversion factor.

    Uses the global `CELSIUS_TO_FAHRENHEIT_FACTOR` to perform the conversion.

    Args:
        celsius (float): The temperature in Celsius to convert.

    Returns:
        float: The temperature converted to Fahrenheit.

    Examples:
        >>> convert_to_fahrenheit(0.0)
        32.0
    """

    temperature = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temperature
  
def main():
    """Provides a user interface for converting temperatures between Celsius and Fahrenheit.

    Prompts the user for a temperature value and unit (Celsius or Fahrenheit), validates the
    input, and calls the appropriate conversion function (`convert_to_celsius` or
    `convert_to_fahrenheit`). Displays the converted temperature or an error message for
    invalid inputs.

    Args:
        None

    Returns:
        None

    Examples:
        Sample interaction:
        Enter the temperature to convert: 100
        Is this temperature in Celsius or Fahrenheit? (C/F): F
        100.0°F is 37.77777777777778°C

    Raises:
        ValueError: If the temperature input is not a numeric value.
    """

    # Prompt the user to enter a temperature and specify whether it’s in Celsius or Fahrenheit.
    # a. Validate temperature input
    while True:
      try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)    # accepts both negative and positive values
        break
      except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

    # b. Validate unit input
    while True:
      celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
      if celsius_or_fahrenheit in ["F", "C"]:
        break
      else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit") 

    # Conversion based on input
    if celsius_or_fahrenheit == 'C':
      result = convert_to_fahrenheit(temperature)
      print(f"{temperature:.1f}°C is {result:.1f}°F")
    else:  # unit == 'F'
      result = convert_to_celsius(temperature)
      print(f"{temperature:.1f}°F is {result:.1f}°C")
      
if __name__ == "__main__":
  main()
  
