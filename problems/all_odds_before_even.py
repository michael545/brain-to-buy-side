"""
If a fair die is rolled infinitely, what is the probability that all odd numbers appear at least once before the first even number appears?
"""
import numpy as np

def simulate_all_odds_before_even():
    seen_odds = set()
    while True:
        roll = np.random.randint(1, 7)
        if roll % 2 == 1:  
            seen_odds.add(roll)
            if len(seen_odds) == 3:  #allhave appeared
                return True
        else:  
            return False

n_simulations = 1_000_000
success_count = 0

for _ in range(n_simulations):
    if simulate_all_odds_before_even():
        success_count += 1

simulated_prob = success_count / n_simulations

theoretical_prob = 1 / 36

print(f"Simulated probability after {n_simulations:,} trials: {simulated_prob:.6f}")
print(f"Theoretical probability: {theoretical_prob:.6f}")
print(f"Difference: {abs(simulated_prob - theoretical_prob):.6f}")
