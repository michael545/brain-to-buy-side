"""
A fair six-sided die is rolled once. We then continue rolling until we get a
number different from the first roll. What is the expected total sum of all
dice rolls?
"""
import numpy as np
import matplotlib.pyplot as plt

def simulate_roll_sequence():

    first_roll = np.random.randint(1, 7)
    total_sum = first_roll
    
    while True:
        current_roll = np.random.randint(1, 7)
        total_sum += current_roll
        if current_roll != first_roll:
            break  # Stop when we get a different number
            
    return total_sum

n_simulations = 1_000_000
total_sums = [simulate_roll_sequence() for _ in range(n_simulations)]

# --- Results ---
simulated_mean = np.mean(total_sums)
#Theory alone
# E[first_roll] = 3.5
# E[subsequent_rolls] = E[rolls until different] * E[value of any roll]
# Number of subsequent rolls follows a geometric distribution with p=5/6.
# E[number of subsequent rolls] = 1/p = 1/(5/6) = 1.2
# E[total] = E[first_roll] + E[number of subsequent rolls] * E[value of any roll]
# E[total] = 3.5 + 1.2 * 3.5 = 3.5 * (1 + 1.2) = 3.5 * 2.2 = 7.7
theoretical_mean = 7.7

print(f"Simulated expected total sum after {n_simulations:,} trials: {simulated_mean:.6f}")
print(f"Theoretical expected total sum: {theoretical_mean:.6f}")
print(f"Difference: {abs(simulated_mean - theoretical_mean):.6f}")

plt.figure(figsize=(12, 7))
bins = range(min(total_sums), max(total_sums) + 2)
plt.hist(total_sums, bins=bins, density=True, alpha=0.75, color='mediumpurple', edgecolor='black')

plt.axvline(simulated_mean, color='red', linestyle='--', linewidth=2,
            label=f'Simulated Mean: {simulated_mean:.4f}')
plt.axvline(theoretical_mean, color='blue', linestyle=':', linewidth=2,
            label=f'Theoretical Mean: {theoretical_mean:.4f}')

plt.title('Distribution of Total Sum (Roll Until Different)')
plt.xlabel('Total Sum of Rolls')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()