import numpy as np
import matplotlib.pyplot as plt

# HW3 #9: Count arrivals in sub-interval of length 1
print("Problem 9: Count arrivals in sub-interval of length 1\n")

lambda_rate = 5
n_trials = 1000
counts = []
for _ in range(n_trials):
    inter_arrivals = np.random.exponential(1/lambda_rate, 1000)
    arrival_times = np.cumsum(inter_arrivals)
    # count arrivals in interval [3,4]
    counts.append(np.sum((arrival_times >= 3) & (arrival_times < 4)))

# Empirical PMF
values, freqs = np.unique(counts, return_counts=True)
pmf_empirical = freqs / n_trials

# Theoretical Poisson(λ=5*1) = Poisson(5)
from math import exp, factorial
pmf_theoretical = [exp(-5) * 5**k / factorial(k) for k in values]

plt.figure(figsize=(10, 6))
plt.plot(values, pmf_empirical, 'ro-', label="Simulation Results", markersize=6)
plt.plot(values, pmf_theoretical, 'bo-', label="Theoretical", markersize=6)
plt.xlabel("X")
plt.ylabel("Probability")
plt.title("PMF of Poisson distribution (λ=5)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
