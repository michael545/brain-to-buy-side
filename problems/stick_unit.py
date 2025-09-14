"""
A stick of unit length is broken at two random points.
What is the probability that the three resulting segments can form a triangle?

For a triangle to be formed, the triangle inequality must hold: the sum of the
lengths of any two sides must be greater than the length of the third.
For a stick of length 1, this simplifies to the condition that no single
segment can have a length greater than 0.5.
"""
import numpy as np
import matplotlib.pyplot as plt

def simulate_stick_break():
    # Simulates breaking a stick at two random points and checks if the
    # resulting three segments can form a triangle.
    # Generate two random break points along the stick
    break_points = np.random.uniform(0, 1, 2)
    break_points.sort()
    
    p1, p2 = break_points[0], break_points[1]
    
    # Calculate the lengths of the three segments
    segment1 = p1
    segment2 = p2 - p1
    segment3 = 1 - p2
    
    # Check if any segment is longer than 0.5. If so, no triangle.
    if segment1 > 0.5 or segment2 > 0.5 or segment3 > 0.5:
        return False  # Cannot form a triangle
    else:
        return True   # Can form a triangle

n_simulations = 1_000_000
can_form_triangle_count = 0

for _ in range(n_simulations):
    if simulate_stick_break():
        can_form_triangle_count += 1

simulated_prob = can_form_triangle_count / n_simulations
theoretical_prob = 0.25

print(f"Simulated probability after {n_simulations:,} trials: {simulated_prob:.6f}")
print(f"Theoretical probability: {theoretical_prob:.6f}")
print(f"Difference: {abs(simulated_prob - theoretical_prob):.6f}")

# --- Visualization of Break Points ---
# Generate sample points for plotting
n_plot = 2000
points = np.random.uniform(0, 1, (n_plot, 2))
can_form = []
for p in points:
    p.sort()
    can_form.append(not (p[0] > 0.5 or (p[1]-p[0]) > 0.5 or (1-p[1]) > 0.5))

can_form = np.array(can_form)

plt.figure(figsize=(8, 8))
plt.scatter(points[can_form, 0], points[can_form, 1], color='green', alpha=0.5, label='Forms a Triangle')
plt.scatter(points[~can_form, 0], points[~can_form, 1], color='red', alpha=0.5, label='Does Not Form a Triangle')
plt.title('Sample Space of Two Break Points on a Stick')
plt.xlabel('Break Point 1')
plt.ylabel('Break Point 2')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()