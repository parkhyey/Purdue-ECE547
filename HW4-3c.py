# HW4 (3c): Plot PB = pN for M/M/1/N
# Requirements: numpy, matplotlib

import numpy as np
import matplotlib.pyplot as plt

def pN_MM1N(rho, N):
    """
    Blocking probability p_N for M/M/1/N:
      p_N = (1 - rho) * rho**N / (1 - rho**(N+1))   if rho != 1
      p_N = 1 / (N + 1)                              if rho == 1
    Accepts scalar or numpy array rho.
    """
    rho = np.asarray(rho, dtype=float)
    out = np.empty_like(rho)

    mask1 = np.isclose(rho, 1.0)
    out[mask1] = 1.0 / (N + 1)

    mask2 = ~mask1
    r = rho[mask2]
    out[mask2] = (1 - r) * (r**N) / (1 - r**(N + 1))
    return out

print("HW4, 3-(c)")

# ---- parameters ----
rhos = np.linspace(0.0, 5.0, 501)   # rho ∈ [0, 5]
Ns = [4, 19]

# ---- compute and plot ----
plt.figure()
for N in Ns:
    plt.plot(rhos, pN_MM1N(rhos, N), label=f"N={N}")

plt.title(r"$P_B = p_N$ (M/M/1/N)")
plt.xlabel(r"$\rho = \lambda/\mu$")
plt.ylabel(r"$P_B = p_N$")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("pb_vs_rho_MM1N.png", dpi=160)
plt.show()

# quick sanity check at rho=1
for N in Ns:
    print(f"N={N}: pN(ρ=1) = {pN_MM1N(1.0, N):.6f} (should be 1/(N+1) = {1/(N+1):.6f})")
