# Purdue ECE547 HW3 #8
import numpy as np
import math
import matplotlib.pyplot as plt

# Function from HW2 #6
def generate_exponential_sample(lambda_rate):
    """Generate single exponential sample using inverse transform"""
    u = np.random.rand()
    return -math.log(1 - u) / lambda_rate

# Problem 8: Poisson process N(t) with rate 5
print("=== Problem 8: Poisson Process N(t) ===")

lambda_rate = 5      # arrival rate
sim_time = 30.0      # total simulation time

# Generate arrival times using exponential inter-arrivals
arrival_times = []
t = 0.0
while t < sim_time:
    inter_arrival = generate_exponential_sample(lambda_rate)
    t += inter_arrival
    if t < sim_time:
        arrival_times.append(t)

print(f"Generated {len(arrival_times)} arrivals in {sim_time} seconds")
print(f"Average arrival rate: {len(arrival_times)/sim_time:.3f} arrivals/sec")

# Construct N(t) over a time grid
t_plot = np.linspace(0, sim_time, 1000)
N_t = []
for ti in t_plot:
    count = sum(1 for at in arrival_times if at <= ti)
    N_t.append(count)

# Plot N(t)
plt.figure(figsize=(10, 6))
plt.step(t_plot, N_t, where='post', linewidth=1.5)
plt.xlabel('Time (s)')
plt.ylabel('N(t)')
plt.title(' N(t) of Posson process (λ=5)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
