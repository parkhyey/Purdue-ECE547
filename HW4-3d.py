# HW4 (3d): Plot normalized throughput gamma/mu for M/M/1/N
# Requirements: numpy, matplotlib

import numpy as np
import matplotlib.pyplot as plt

def pN_MM1N(rho, N):
    """
    Blocking probability p_N for M/M/1/N:
      p_N = (1 - rho) * rho**N / (1 - rho**(N+1))   if rho != 1
      p_N = 1 / (N + 1)                              if rho == 1
    Supports scalar or numpy array rho.
    """
    rho = np.asarray(rho, dtype=float)
    out = np.empty_like(rho)

    is_one = np.isclose(rho, 1.0)
    out[is_one] = 1.0 / (N + 1)

    r = rho[~is_one]
    out[~is_one] = (1 - r) * (r**N) / (1 - r**(N + 1))
    return out

def throughput_norm(rho, N):
    """Normalized throughput gamma/mu = rho * (1 - p_N)."""
    return rho * (1 - pN_MM1N(rho, N))

print("HW4, 3-(d)")

# ---- parameters ----
rhos = np.linspace(0.0, 5.0, 501)   # rho ∈ [0, 5]
Ns = [4, 19]

# ---- compute & plot ----
plt.figure()
for N in Ns:
    plt.plot(rhos, throughput_norm(rhos, N), label=f"N={N}")

plt.title(r"Normalized Throughput $\gamma/\mu$")
plt.xlabel(r"$\rho = \lambda/\mu$")
plt.ylabel(r"$\gamma/\mu$")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("hw4_3d_throughput.png", dpi=160)  # optional: saves figure
plt.show()

# ---- quick sanity checks ----
for N in Ns:
    # At rho=1, pN = 1/(N+1)  => gamma/mu = 1 - 1/(N+1) = N/(N+1)
    val = throughput_norm(1.0, N)
    print(f"N={N}: gamma/mu at rho=1 = {val:.6f} (expected {N/(N+1):.6f})")
