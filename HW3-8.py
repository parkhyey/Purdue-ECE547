import numpy as np
import matplotlib.pyplot as plt
import math

# Function from HW2 #6
def generate_exponential_sample(lambda_rate):
    """Generate single exponential sample using inverse transform"""
    u = np.random.rand()
    return -math.log(1 - u) / lambda_rate

# HW3 #8: Generate Poisson process N(t) with rate λ=5
print("Problem 8: Poisson process N(t) with rate λ=5")

lambda_rate = 5
n_events = 200   # number of arrivals to simulate

# Generate inter-arrival times using HW2 method
inter_arrivals = [generate_exponential_sample(lambda_rate) for _ in range(n_events)]
arrival_times = np.cumsum(inter_arrivals)

# Plot Poisson process N(t)
plt.figure(figsize=(10, 6))
plt.step(arrival_times, np.arange(1, n_events+1), where='post', linewidth=1.5)
plt.xlabel("t (second)")
plt.ylabel("N(t)")
plt.title("N(t) of Poisson Process (λ=5)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
