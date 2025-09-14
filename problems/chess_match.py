"""
32 players are participating in a chess tournament. In each round 2 players compete against each other.
The winner advances to the next round, while the loser is eliminated.
This continues until only one player remains, who is declared the champion.
What is the probability that two players face each other in a match assume they all have same skill?
"""
import numpy as np

def simulate_tournament_meet(n_players=32, player_a=0, player_b=1):
    """
    Simulates a single-elimination tournament with a fixed bracket
    to see if two specific players meet.
    """
    players = list(range(n_players))
    np.random.shuffle(players)
    
    while len(players) > 1:
        next_round_winners = []
        for i in range(0, len(players), 2):
            p1 = players[i]
            p2 = players[i+1]
            
            if (p1 == player_a and p2 == player_b) or \
               (p1 == player_b and p2 == player_a):
                return True  # They met
            
            winner = np.random.choice([p1, p2])
            next_round_winners.append(winner)
        
        players = next_round_winners
        
    return False


n_simulations = 100000
meet_count = 0

for _ in range(n_simulations):
    if simulate_tournament_meet():
        meet_count += 1

simulated_prob = meet_count / n_simulations

theoretical_prob = 2 / 32

print(f"Simulated probability after {n_simulations:,} trials: {simulated_prob:.6f}")
#print(f"Theoretical probability (2/N): {theoretical_prob:.6f}")