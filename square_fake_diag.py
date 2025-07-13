import numpy as np
import matplotlib.pyplot as plt


'''we have square in this square we randomly select a point and connect it to the bottom left vertex (0,0) we select anotther random point and connect it to the top left vertex (0,1).
Depending on the location of the two points these two lines may or may not intersect.
 What is the probability that these two lines intersect?'''
n_simulations = 100000
intersections = 0


def lines_intersect(p1, p2):
    """Check if line from p1 to (0,0) intersects line from p2 to (0,1)"""
    x1, y1 = p1
    x2, y2 = p2
    
    return x1 < x2 and y1 > y2


def lines_intersect_test(p1, p2):
    """Check if line from p1 to (0,0) intersects line from p2 to (0,1)"""
    x1, y1 = p1
    x2, y2 = p2
    k1 = y1 / x1 if x1 != 0 else np.inf  # Avoid division by zero
    k2 = -(1-y2) / x2 if x2 != 0 else np.inf  # Avoid division by zero

    x_intersect = 1.0 / (k1 - k2)
    return np.isfinite(x_intersect) and (x_intersect > 0) and (x_intersect <= min(x2, x1))

for _ in range(n_simulations):
    p1 = np.random.uniform(0, 1, 2)  # Random point in unit square
    p2 = np.random.uniform(0, 1, 2)  # Random point in unit square

    if lines_intersect_test(p1, p2):
        intersections += 1

probability = intersections / n_simulations

# Plot sample
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

# Draw sample lines
for _ in range(50):
    p1 = np.random.uniform(0, 1, 2)
    p2 = np.random.uniform(0, 1, 2)
    
    color = 'red' if lines_intersect(p1, p2) else 'blue'
    ax.plot([p1[0], 0], [p1[1], 0], color=color, alpha=0.3, linewidth=0.5)
    ax.plot([p2[0], 0], [p2[1], 1], color=color, alpha=0.3, linewidth=0.5)

ax.plot(0, 0, 'ko', markersize=8, label='Bottom-left (0,0)')
ax.plot(0, 1, 'ko', markersize=8, label='Top-left (0,1)')
ax.set_title(f'P(lines intersect) ≈ {probability:.4f}')
ax.legend()
ax.grid(True, alpha=0.3)
plt.show()

print(f"Probability of intersection: {probability:.6f}")
print(f"Theoretical value: 1/3 = {1/3:.6f}")