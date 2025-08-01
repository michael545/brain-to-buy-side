"""
 six-sided die is rolled 10 times.
for each face i ∈ {1,2,...,6}, let Nᵢ denote the number of times face i appears.
get the expected value E[N₁N₂N₃N₄N₅N₆].
"""
import numpy as np
import matplotlib.pyplot as plt

def simulate_product():
    rolls = np.random.randint(1, 7, 10)
    counts = np.bincount(rolls, minlength=7)[1:]  # Count occurrences of each face (1-6)
    return np.prod(counts)

n_simulations = 1000000
products = [simulate_product() for _ in range(n_simulations)]
sim_mean = np.mean(products)

plt.figure(figsize=(10, 6))
plt.hist(products, bins=50, density=True, alpha=0.7, color='purple', edgecolor='black')
plt.axvline(sim_mean, color='red', linestyle='--', linewidth=2, 
            label=f'Simulated Mean: {sim_mean:.4f}')
plt.xlabel('Product N₁N₂N₃N₄N₅N₆')
plt.ylabel('Density')
plt.title('Distribution of Product N₁N₂N₃N₄N₅N₆ (10 die rolls)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print(f"Expected value E[N₁N₂N₃N₄N₅N₆]: {sim_mean:.6f}")