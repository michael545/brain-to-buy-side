"""
Six points are chosen at random on the circumference of a circle.
What is the probability that all six points lie on a single semicircular arc?
"""
import numpy as np
import matplotlib.pyplot as plt

def check_semicircle_condition(num_points=6):

    points = np.random.uniform(0, 2*np.pi, num_points)
    points.sort()

    gaps = np.diff(points)

    wrap_around_gap = (2 * np.pi - points[-1]) + points[0]
    
    max_gap = np.max(np.append(gaps, wrap_around_gap))
    
    return max_gap >= np.pi


n_simulations = 100_000
success_count = 0

for _ in range(n_simulations):
    if check_semicircle_condition():
        success_count += 1

simulated_prob = success_count / n_simulations

# For N points,theroy is is N * (1/2)^(N-1).
# For 6 points, it's 6 * (1/2)^5 = 6 / 32 = 3 / 16.
theoretical_prob = 6 * (1/2)**5

print(f"Simulated probability after {n_simulations:,} trials: {simulated_prob:.6f}")
print(f"Theoretical probability (6 * (1/2)^5): {theoretical_prob:.6f} or 3/16")
print(f"Difference: {abs(simulated_prob - theoretical_prob):.6f}")

