# HW4 (2c): Plot E[n] vs rho for an M/M/1 queue
# X-axis: 0 to 1, Y-axis: 0 to 10, no asymptote line

import numpy as np
import matplotlib.pyplot as plt

def En_MM1(rho):
    """
    Expected number in system for M/M/1 queue:
        E[n] = rho / (1 - rho), for 0 <= rho < 1
    Returns NaN if rho >= 1 (unstable).
    """
    rho = np.asarray(rho, dtype=float)
    out = np.full_like(rho, np.nan, dtype=float)
    mask = (rho >= 0) & (rho < 1)
    out[mask] = rho[mask] / (1 - rho[mask])
    return out

print("HW4, 2-(c)")

# Define rho values
rhos = np.linspace(0.0, 0.999, 600)
En_vals = En_MM1(rhos)

# Plot
plt.figure(figsize=(7,5))
plt.plot(rhos, En_vals, linewidth=2, color="blue")

# Set requested axis ranges
plt.xlim(0.0, 1.0)
plt.ylim(0, 10)

plt.xlabel(r"$\rho = \lambda/\mu$")
plt.ylabel(r"$E[n]$")
plt.grid(True)
plt.tight_layout()
plt.show()
