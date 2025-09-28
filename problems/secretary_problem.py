import numpy as np

def simulate_secretary_problem(n_candidates, n_simulations):
    successes = 0
    for _ in range(n_simulations):
        # Generate a random permutation of candidates
        candidates = np.random.permutation(n_candidates)
        # Determine the optimal stopping point
        stop_point = int(n_candidates / np.e)
        # Find the best candidate among the first 'stop_point' candidates
        best_so_far = max(candidates[:stop_point])
        # Find the first candidate after 'stop_point' that is better than 'best_so_far'
        for candidate in candidates[stop_point:]:
            if candidate > best_so_far:
                if candidate == n_candidates:  # Assuming the highest number represents the best candidate
                    successes += 1
                break
    return successes / n_simulations

n_candidates = 100  # Number of candidates
n_simulations = 100000  # Number of simulations
probability = simulate_secretary_problem(n_candidates, n_simulations)
print(f"Estimated probability of selecting the best candidate: {probability:.4f}")
