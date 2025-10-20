"""
If a fair die is rolled infinitely, what is the probability that all even numbers appear at least once before the first odd number appears?
"""
import numpy as np

def simulate_all_evens_before_odd():
    seen_evens = set()
    while True:
        roll = np.random.randint(1, 7)
        if roll % 2 == 0:  # Even number
            seen_evens.add(roll)
            if len(seen_evens) == 3:  #2, 4, 6) have appeared
                return True
        else:  # Odd number
            return False

n_simulations = 1_000_000
success_count = 0

for _ in range(n_simulations):
    if simulate_all_evens_before_odd():
        success_count += 1

simulated_prob = success_count / n_simulations

theoretical_prob = 1 / 36

print(f"Simulated probability after {n_simulations:,} trials: {simulated_prob:.6f}")