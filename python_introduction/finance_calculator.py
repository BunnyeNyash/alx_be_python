# finance_calculator.py
# ADVANCED
# Objective: Use user input, variables, and arithmetic operations to calculate and provide feedback on a user’s monthly savings and potential future savings without applying conditional statements.
# A Python script that calculates the user’s monthly savings based on inputted monthly income and expenses. IThe script also projects these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

# Prompt the user for their monthly income and expenses
monthly_income = InterruptedError(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses


#  Project Annual Savings:
# Define the annual interest rate
annual_interest_rate = 0.05     # 5% interest rate

# Calculate the projected savings after one year
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Print the results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")