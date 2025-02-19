# Medina Kubanychbekova
# Date: 02/19/2025
# Problem 4: Approximate Pi and compare it to math.pi

import math

# Using the Gregory-Leibniz series (simplified for a few terms)
def approximate_pi(n_terms=1000):
    pi_approx = sum((-1)**k / (2*k + 1) for k in range(n_terms)) * 4
    return pi_approx

approx_pi = approximate_pi()
print(f"Approximated Pi: {approx_pi}")
print(f"Actual Pi from math module: {math.pi}")
