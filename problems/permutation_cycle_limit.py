import numpy as np

def has_long_cycle(permutation):
    num_elements = len(permutation)
    n = num_elements // 2
    visited = [False] * num_elements

    for i in range(num_elements):
        if not visited[i]:
            cycle_length = 0
            current = i
            while not visited[current]:
                visited[current] = True
                current = permutation[current]
                cycle_length += 1

            if cycle_length > n:
                return True
    return False

n = 100       
num_trials = 50000 # Number of random shuffles to perform

print(f" sim for n = {n} w {num_trials} trials...")

long_cycle_count = 0
for _ in range(num_trials):
    # Generate a random permutation of {0, 1, ..., 2n-1}
    p = np.random.permutation(2 * n)
    if has_long_cycle(p):
        long_cycle_count += 1

simulated_prob = long_cycle_count / num_trials
ln2 = np.log(2)
print(f"\n howm any (long cycles found): {long_cycle_count}")
print(f"Simulated probability: {simulated_prob:.6f}")
print(f"theory alone: {ln2:.6f}")