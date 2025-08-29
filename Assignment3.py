# Task 1

# Factorial
def factorial_recursion(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)

num = int(input("Enter a number: "))

print(f"Factorial of {num} is: {factorial_recursion(num)}")

# Task2

import math  # Import the math module


num = float(input("Enter a number: "))

square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)


print(f"Square root: {square_root}")
print(f"logarithm: {natural_log}")
print(f"Sine: {sine_value}")
