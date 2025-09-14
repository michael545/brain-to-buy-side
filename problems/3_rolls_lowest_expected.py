"""
Rolling 3 fair 100-sided dice, what is the expected value of the lowest roll?
"""
import numpy as np
import matplotlib.pyplot as plt

def simulate_lowest_roll():
    rolls = np.random.randint(1, 101, 3)
    return np.min(rolls)

n_simulations = 100000
lowest_rolls = [simulate_lowest_roll() for _ in range(n_simulations)]
sim_mean = np.mean(lowest_rolls)
theory_mean = sum(k * (k**3 - (k-1)**3) / 100**3 for k in range(1, 100))

plt.figure(figsize=(10, 6))
plt.hist(lowest_rolls, bins=range(1, 102), density=True, alpha=0.7, color='orange', edgecolor='black')
plt.axvline(sim_mean, color='red', linestyle='--', linewidth=2, 
            label=f'Simulated Mean: {sim_mean:.4f}')
plt.axvline(theory_mean, color='blue', linestyle=':', linewidth=2, 
            label=f'Theoretical Mean: {theory_mean:.4f}')
plt.xlabel('Lowest Roll Value')
plt.ylabel('Probability')
plt.title('Distribution of Lowest Roll from 3 Fair 100-sided Dice')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
