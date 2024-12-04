import numpy as np
from scipy.integrate import quad

# Define the parameterized function for the line integral
# Circle parameterization: x = sqrt(3) * cos(t), y = sqrt(3) * sin(t)
def integrand(t):
    x = np.sqrt(3) * np.cos(t)
    y = np.sqrt(3) * np.sin(t)
    dx_dt = -np.sqrt(3) * np.sin(t)
    dy_dt = np.sqrt(3) * np.cos(t)
    ds_dt = np.sqrt(dx_dt**2 + dy_dt**2)  # Arc length element
    return (x**2 + y**4) * ds_dt

# Integrate over the full circle (0 to 2*pi)
result, _ = quad(integrand, 0, 2 * np.pi)

# Print the result
print(f"Line integral result: {result}")

"""
Line integral result: 53.05363140385086
"""