"""
You roll a fair six-sided die repeatedly. What is the expected number of rolls
required to see all six faces (1, 2, 3, 4, 5, and 6) at least once
Coupon Collector's Problem.
"""
import numpy as np
import matplotlib.pyplot as plt

def simulate_rolls_for_all_faces():
    seen_faces = set()
    num_rolls = 0
    while len(seen_faces) < 6:
        roll = np.random.randint(1, 7)
        seen_faces.add(roll)
        num_rolls += 1
    return num_rolls

# --- Simulation ---
n_simulations = 100_000
roll_counts = [simulate_rolls_for_all_faces() for _ in range(n_simulations)]

# --- Results ---
simulated_mean = np.mean(roll_counts)

# The theoretical expected number of rolls to collect N coupons is N * H_N,
# where H_N is the N-th Harmonic Number.
# For a 6-sided die, N=6. E = 6 * (1/1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6)
theoretical_mean = 6 * sum(1/i for i in range(1, 7))

print(f"Simulated expected number of rolls after {n_simulations:,} trials: {simulated_mean:.6f}")
print(f"Theoretical expected number of rolls: {theoretical_mean:.6f}")
print(f"Difference: {abs(simulated_mean - theoretical_mean):.6f}")

# --- Plotting ---
plt.figure(figsize=(12, 7))
plt.hist(roll_counts, bins=range(min(roll_counts), max(roll_counts) + 2),
         density=True, alpha=0.75, color='darkcyan', edgecolor='black')

plt.axvline(simulated_mean, color='red', linestyle='--', linewidth=2,
            label=f'Simulated Mean: {simulated_mean:.4f}')
plt.axvline(theoretical_mean, color='blue', linestyle=':', linewidth=2,
            label=f'Theoretical Mean: {theoretical_mean:.4f}')

plt.title('Distribution of Rolls Needed to See All 6 Faces')
plt.xlabel('Number of Rolls')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()