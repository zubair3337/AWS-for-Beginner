# modules.py
# Example of using the math module in Python

import math  # importing the math module (toolbox for math functions)

# Example 1: absolute value
x = -7.5
abs_value = math.fabs(x)
print(f"Absolute value of {x} using math.fabs() is {abs_value}")

# Example 2: floor function
y = 4.8
floor_value = math.floor(y)
print(f"Floor value of {y} using math.floor() is {floor_value}")

# Extra Challenge 1: customize print statement
print(f"I used math.fabs() to turn a negative number ({x}) into positive ({abs_value}).")
print(f"I used math.floor() to round {y} down to the nearest integer ({floor_value}).")

# Extra Challenge 2: What happens if we try to put a string into math.floor?
try:
    test_value = "hello"
    result = math.floor(test_value)  # this will cause an error
    print(result)
except TypeError as e:
    print(f"Error: You cannot use math.floor() on a string. Details: {e}")
