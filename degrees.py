# Medina Kubanychbekova
# Date: 02/19/2025
# Problem 5: Convert radians to degrees

import math

# Get user input in radians
radians = float(input("Enter the value in radians: "))

# Manual conversion formula
degrees_manual = radians * (180 / math.pi)

# Using math.degrees()
degrees_math_module = math.degrees(radians)

print(f"Converted Degrees (Manual Calculation): {degrees_manual}")
print(f"Converted Degrees (Using math.degrees()): {degrees_math_module}")
