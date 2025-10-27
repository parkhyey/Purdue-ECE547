import numpy as np
import math
from collections import defaultdict
import matplotlib.pyplot as plt

# --- helper (from HW3 code) ---
def generate_exponential_sample(rate):
    u = np.random.rand()
    return -math.log(1 - u) / rate

# Parameters
lam, mu = 5.0, 6.0
rho = lam / mu
T_end = 20000

# State
t, n, queue, server_busy = 0.0, 0, 0, False
t_next_arrival = generate_exponential_sample(lam)
t_next_departure = math.inf
time_in_state = defaultdict(float)

while True:
    t_event = min(t_next_arrival, t_next_departure)
    if t_event > T_end:
        time_in_state[n] += T_end - t
        break
    time_in_state[n] += t_event - t
    t = t_event

    if t_next_arrival <= t_next_departure:
        n += 1
        if not server_busy:
            server_busy = True
            t_next_departure = t + generate_exponential_sample(mu)
        else:
            queue += 1
        t_next_arrival = t + generate_exponential_sample(lam)
    else:
        n -= 1
        if queue > 0:
            queue -= 1
            t_next_departure = t + generate_exponential_sample(mu)
        else:
            server_busy = False
            t_next_departure = math.inf

# Normalize probabilities
total_time = sum(time_in_state.values())
p_sim = {k: v/total_time for k, v in time_in_state.items()}
En_sim = sum(k * p_sim[k] for k in p_sim)

# Theory
En_the = rho / (1 - rho)

print("HW4-8")

# --- Print results ---
# print(f"rho = {rho:.3f}")
print(f"E[n]_simulation = {En_sim:.4f}, E[n]_theory = {En_the:.4f}")
print("\nn   Pn_sim     Pn_theory")
for n in range(6):  # first few states
    p_the = (1 - rho) * rho**n
    print(f"{n:<2d}  {p_sim.get(n,0):.4f}    {p_the:.4f}")

# --- Graph comparison (simulation vs theory) ---
N_report = max(20, max(p_sim.keys()))  # show up to 20 or max observed
x = np.arange(N_report + 1)
emp_pn = [p_sim.get(k, 0) for k in x]
the_pn = [(1 - rho) * (rho ** k) for k in x]

plt.figure()
plt.plot(x, emp_pn, marker='o', linestyle='-', label='Simulation')
plt.plot(x, the_pn, marker='x', linestyle='--', label='Theory')
plt.xlabel('n')
plt.ylabel('Pn')
plt.title('M/M/1 (λ=5, μ=6): Pn Simulation vs Theory')
plt.legend()
plt.show()
