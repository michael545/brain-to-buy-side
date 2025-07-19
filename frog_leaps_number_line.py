"""
A frog begins at position 100 on a number line.
Every second, if the frog is at position x > 1,
it jumps to a randomly chosen integer position between
1 and x - 1 (inclusive).
What is the expected number of seconds until the frog
reaches position 1?
"""

import numpy as np
import matplotlib.pyplot as plt


def simulate_frog_jumps(start_position: int) -> int:
    position = start_position
    jumps = 0
    while position > 1:
        # top bound of randint is exclusive
        position = np.random.randint(1, position)
        jumps += 1
    return jumps

n_simulations = 40000
start_pos = 100

jump_counts = [simulate_frog_jumps(start_pos) for _ in range(n_simulations)]
sim_mean = np.mean(jump_counts)
theory_mean = sum(1/i for i in range(1, start_pos)) #same as H_99

plt.figure(figsize=(12, 7))
plt.hist(jump_counts, bins=range(min(jump_counts), max(jump_counts) + 1), 
         density=True, alpha=0.75, color='green', edgecolor='black',
         label='Simulation Results')
plt.axvline(sim_mean, color='red', linestyle='--', lw=2, 
            label=f'Simulated Mean: {sim_mean:.4f}')
plt.axvline(theory_mean, color='blue', linestyle=':', lw=2, 
            label=f'Theoretical Mean (H_99): {theory_mean:.4f}')
plt.title(f'Distribution of Jumps for Frog to Reach 1 from {start_pos}')
plt.xlabel('Number of Jumps')
plt.ylabel('PDF')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print(f"""
Simulation ({n_simulations:,} trials):
  Expected Jumps: {sim_mean:.6f}

Theoretical (H_99):
  Expected Jumps: {theory_mean:.6f}
""")
