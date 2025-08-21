"""
ew have 12 coins in 4 rows of 3. Each row has a different
probability of landing heads:
- Row 1 (3 coins): P(H) = 1/2
- Row 2 (3 coins): P(H) = 1/3
- Row 3 (3 coins): P(H) = 1/5
- Row 4 (3 coins): P(H) = 1/9
What is the probability that the total number of heads is odd?
"""
import numpy as np

def simulate_odd_heads():
    """
    Simulates one trial of flipping all 12 coins and returns
    True if the total number of heads is odd, False otherwise.
    """
    # Probabilities for each of the 12 coins
    probabilities = [1/2]*3 + [1/3]*3 + [1/5]*3 + [1/9]*3
    
    total_heads = 0
    for p in probabilities:
        # np.random.rand() gives a float in [0.0, 1.0)
        if np.random.rand() < p:
            total_heads += 1
            
    # Return True if total_heads is odd (e.g., 1, 3, 5...)
    return total_heads % 2 != 0

# --- Simulation ---
n_simulations = 1_000_000
odd_count = 0

for _ in range(n_simulations):
    if simulate_odd_heads():
        odd_count += 1

# --- Results ---
simulated_prob = odd_count / n_simulations

theoretical_prob = 0.5

print(f"Sim after {n_simulations:,} scenarios: {simulated_prob:.6f}")
print(f"Theory: {theoretical_prob:.6f}")
#print(f"Delta: {abs(simulated_prob - theoretical_prob):.6f}")
