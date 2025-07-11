import numpy as np
import matplotlib.pyplot as plt

def find_arc_containing_point(angles, target_angle=0.0): #target_angle is the angle of the point (1,0)
    angles = np.sort(angles)
    arc_lengths = [angles[1] - angles[0], 
                   angles[2] - angles[1], 
                   2*np.pi - (angles[2] - angles[0])]
    
    if angles[0] <= target_angle <= angles[1]:
        return arc_lengths[0]
    elif angles[1] <= target_angle <= angles[2]:
        return arc_lengths[1]
    else:
        return arc_lengths[2]

# simulation
n_simulations = 100000
arc_lengths = []

for _ in range(n_simulations):
    random_angles = np.random.uniform(0, 2*np.pi, 3)
    arc_length = find_arc_containing_point(random_angles, 0.0)
    arc_lengths.append(arc_length)

mean_length = np.mean(arc_lengths)
print(f'arc len containing (1,0): {mean_length:.4f} radians')

# Plot
plt.figure(figsize=(10, 6))
plt.hist(arc_lengths, bins=50, density=True, alpha=0.7, color='skyblue', edgecolor='black')
plt.axvline(mean_length, color='red', linestyle='--', linewidth=2, 
            label=f'Mean: {mean_length:.4f} radians')
plt.xlabel('Arc Length (radians)')
plt.ylabel('Density')
plt.title('Distribution of Arc Lengths Containing (1,0)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()