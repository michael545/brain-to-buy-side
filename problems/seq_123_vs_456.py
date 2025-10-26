
import numpy as np

def simulate_seq_123_vs_456():
    idx_123 = 0
    idx_456 = 0
    seq_123 = [1, 2, 3]
    seq_456 = [4, 5, 6]
    while True:
        roll = np.random.randint(1, 7)
        if roll == seq_123[idx_123]:
            idx_123 += 1
            if idx_123 == 3:
                return 1  # 1,2,3 appeared in order first
        if roll == seq_456[idx_456]:
            idx_456 += 1
            if idx_456 == 3:
                return 2  # 4,5,6 appeared in order first
n_simulations = 1000; seq_123_first = 0


for _ in range(n_simulations):
    if simulate_seq_123_vs_456() == 1:
        seq_123_first += 1

simulated_prob = seq_123_first / n_simulations

print(f"Simulated probability that 1,2,3 appears before 4,5,6: {simulated_prob:.6f}")