import numpy as np
import matplotlib.pyplot as plt
import heapq
import math

def generate_exponential_sample(lambda_rate):
    """Generate exponential sample using HW2 inverse transform method"""
    u = np.random.rand()
    return -math.log(1 - u) / lambda_rate

def simulate_queue(lambda_rate=5, mu=10, sim_time=50):
    t = 0
    n = 0
    timeline = []
    events = []  # (time, type) where type = 'arrival' or 'departure'

    # schedule first arrival using HW2 method
    heapq.heappush(events, (generate_exponential_sample(lambda_rate), 'arrival'))

    while t < sim_time and events:
        t, etype = heapq.heappop(events)

        if etype == 'arrival':
            n += 1
            # schedule next arrival using HW2 method
            heapq.heappush(events, (t + generate_exponential_sample(lambda_rate), 'arrival'))
            # if server idle, schedule departure (deterministic service time)
            if n == 1:
                heapq.heappush(events, (t + 1/mu, 'departure'))

        elif etype == 'departure':
            n -= 1
            if n > 0:  # if queue not empty, schedule next departure
                heapq.heappush(events, (t + 1/mu, 'departure'))

        timeline.append((t, n))

    return np.array(timeline)

# HW3 #10: Queue simulation with different service rates
print("Problem 10: Queue Simulation with different service rates\n")

plt.figure(figsize=(12, 8))

# Run simulation for different service rates
service_rates = [10, 6, 4]
colors = ['blue', 'green', 'red']

for i, mu in enumerate(service_rates):
    print(f"\nService rate μ = {mu}/s (service time = {1/mu:.4f}s)")
    
    data = simulate_queue(lambda_rate=5, mu=mu, sim_time=50)
    
    # Calculate average queue length
    times = data[:,0]
    queue_lengths = data[:,1]
    avg_queue_length = np.mean(queue_lengths)
    utilization = 5 / mu  # ρ = λ/μ
    
    print(f"Average queue length: {avg_queue_length:.4f}")
    print(f"Utilization ρ = λ/μ: {utilization:.4f}")
    
    if utilization >= 1:
        print("WARNING: System is unstable (ρ ≥ 1)")
    
    plt.step(data[:,0], data[:,1], where='post', 
             label=f"μ={mu} (avg={avg_queue_length:.3f})", 
             color=colors[i], linewidth=1.5)

plt.xlabel("Time (s)")
plt.ylabel("n(t) (number in system)")
plt.title("Problem 10: Queue Dynamics (M/D/1, λ=5)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f"\nSummary:")
print(f"- M/D/1 queue: Poisson arrivals (λ=5), Deterministic service")
print(f"- As service rate μ decreases, queue length increases")
print(f"- When μ < λ, the system becomes unstable")
