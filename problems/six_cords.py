import random
import itertools

def check_intersection(chord1, chord2):
    p1, p2 = sorted(chord1)
    p3, p4 = sorted(chord2)
    
    # The chords intersect if one point of the second chord is between the points
    # of the first chord, and the other is not.
    # This is equivalent to the endpoints interleaving: p1 < p3 < p2 < p4
    # or p3 < p1 < p4 < p2
    return (p1 < p3 < p2 < p4) or (p3 < p1 < p4 < p2)

def has_any_intersection(chords):
    """
    Checks if any pair of chords in a given set intersects.
    """
    # Iterate through all unique pairs of chords
    for chord_a, chord_b in itertools.combinations(chords, 2):
        if check_intersection(chord_a, chord_b):
            return True  # Found an intersection, no need to check further
    return False # No intersections were found

def run_simulation(num_trials=100000):
    """
    Runs the main simulation for a specified number of trials.
    """
    points = list(range(12))
    non_intersecting_count = 0

    print(f"Running simulation for {num_trials:,} trials...")

    for i in range(num_trials):
        # Step 1: Create a random set of 6 chords
        random.shuffle(points)
        chords = []
        for j in range(0, 12, 2):
            chords.append((points[j], points[j+1]))
        
        # Step 2: Check if this set has any intersections
        if not has_any_intersection(chords):
            non_intersecting_count += 1
            
    # Step 3: Calculate the final probability
    estimated_probability = non_intersecting_count / num_trials
    return estimated_probability

# --- Run the simulation ---
trials = 1000000 # Using a large number for better accuracy
simulated_prob = run_simulation(trials)

# --- Display the results ---
theoretical_prob = 4 / 315

print("\n--- Results ---")
print(f"Theoretical Probability: 4/315 ≈ {theoretical_prob:.6f}")
print(f"Simulated Probability ({trials:,} trials): ≈ {simulated_prob:.6f}")
print(f"Difference: {abs(simulated_prob - theoretical_prob):.6f}")