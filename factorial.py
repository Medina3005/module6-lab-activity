# Medina Kubanychbekova
# Date: 02/19/2025
# Problem 6: Compute factorial of a user input value

import math

# Get user input
num = int(input("Enter a number to compute its factorial: "))

# Compute factorial using a loop
factorial_loop = 1
for i in range(1, num + 1):
    factorial_loop *= i

# Compute factorial using math module
factorial_math = math.factorial(num)

print(f"Factorial (Using Loop): {factorial_loop}")
print(f"Factorial (Using math.factorial()): {factorial_math}")
