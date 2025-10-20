# HW4 (2c): Plot E[n] vs rho for an M/M/1 queue
# Requirements: numpy, matplotlib

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

# Define range of rho (avoid 1 because of asymptote)
rhos = np.linspace(0.0, 0.999, 600)
En_vals = En_MM1(rhos)

# Plot
plt.figure()
plt.plot(rhos, En_vals, linewidth=2)
plt.title(r"E[n] vs. $\rho$ for M/M/1")
plt.xlabel(r"$\rho = \lambda/\mu$")
plt.ylabel(r"$E[n]$")
plt.grid(True)
plt.tight_layout()
plt.show()
