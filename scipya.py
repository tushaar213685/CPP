import numpy as np
from scipy.optimize import minimize

# Define the objective function
def objective_function(vars):
    x, y = vars
    return 2 * (x - y - 3)**2 + 4 * (x + 2 * y + 1)**4

# Define the constraints
constraints = [
    {'type': 'ineq', 'fun': lambda vars: vars[0] - vars[1] + 3},  # x - y >= -3
    {'type': 'ineq', 'fun': lambda vars: 5 - ((vars[0] + 2)**2 + (vars[1] + 1)**2)}  # (x + 2)^2 + (y + 1)^2 <= 5
]

# Initial guess for x and y
initial_guess = [0, 0]

# Perform the minimization
result = minimize(objective_function, initial_guess, constraints=constraints)

# Print the results
print("Optimization result:")
print(f"Minimum value of the objective function: {result.fun}")
print(f"Optimal values: x = {result.x[0]}, y = {result.x[1]}")
"""
Optimization result:
Minimum value of the objective function: 7.345026216976594
Optimal values: x = 0.23492503247591015, y = -0.9285148898405146
"""