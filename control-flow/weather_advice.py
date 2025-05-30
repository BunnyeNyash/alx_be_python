# weather_advice.py
# This script will ask the user about the current weather conditions and provide clothing recommendations based on the input. This task aims to demonstrate the use of if, elif, and else statements to make decisions in a program.
# Objective: Utilize conditional statements to guide program execution based on user input regarding weather conditions.

# Prompt User for Weather Input
weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

# Provide Clothing Recommendation
if weather == "sunny":
  recommendation = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
  recommendation = "Don't forget your umbrella and a raincoat."
elif weather == "cold":
  recommendation = "Make sure to wear a warm coat and a scarf."
else:
  recommendation = "Sorry, I don't have recommendations for this weather."

# Output the Recommendation
print(recommendation)
