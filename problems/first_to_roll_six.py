"""
Two players take turns rolling a fair six-sided die. The first player to roll a 6 wins the game.
What is the probability that the first player wins?
"""
import numpy as np

def simulate_game():
    while True:
        # Player 1's turn
        if np.random.randint(1, 7) == 6:
            return 1  # Player 1 wins

        # Player 2's turn
        if np.random.randint(1, 7) == 6:
            return 2  # Player 2 wins

n_simulations = 1_000_000
player1_wins = 0

for _ in range(n_simulations):
    if simulate_game() == 1:
        player1_wins += 1

simulated_prob = player1_wins / n_simulations

theoretical_prob = 6 / 11  # Derived from geometric series

print(f"Simulated probability after {n_simulations:,} trials: {simulated_prob:.6f}")
print(f"Theoretical probability: {theoretical_prob:.6f}")
print(f"Difference: {abs(simulated_prob - theoretical_prob):.6f}")