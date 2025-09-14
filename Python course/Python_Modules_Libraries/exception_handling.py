# Exception Handling Example

try:
    number = int(input("Enter a number: "))
    result = 10 / number   # risky step (possible divide by zero)
    print("Result is:", result)
except ZeroDivisionError:
    print("Oops! You tried to divide by zero (like dividing chocolates among 0 friends).")
except ValueError:
    print("Oops! That was not a number (like writing 'apple' instead of 5).")
finally:
    print("Program ended safely (seatbelt worked).")
