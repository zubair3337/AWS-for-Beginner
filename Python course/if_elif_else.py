

#score = 75

# Taking input from the user
score = int(input("Enter your score: "))

#Checking the grade
if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B!")
elif score >= 70:
    print("You got a C!")
elif score >= 60:
    print("You got a D!")
else:
    print("You failed...")


# second example

 # Taking input for the current gas level in the tank
#gas_level = float(input("Enter the current gas level in the tank (in liters): "))

# Define the low fuel threshold
#low_fuel_threshold = 5.0  # Example: 5 liters

# Check if the gas level is below the threshold
#if gas_level < low_fuel_threshold:
    print("Warning: Low fuel! Please refuel soon.")
else:
    print("Fuel level is sufficient.")


# third exmaple

# Check if the employee has their badge
has_badge = input("Do you have your badge? (yes/no): ")#.strip().lower()

# Decide whether to allow entry or lock the door
if has_badge == "yes":
    print("Access granted. Welcome to the building!")
else:
    print("Access denied. The door is locked.")
