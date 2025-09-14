import numpy as np
from scipy.special import comb 

def run_simulation(n, num_trials=1_000_000):
    alice_coins = n + 2
    bob_coins = n
    
    alice_heads = np.random.binomial(n=alice_coins, p=0.5, size=num_trials)
    bob_heads = np.random.binomial(n=bob_coins, p=0.5, size=num_trials)
    #print(alice_heads[:100], bob_heads[:100]) 
    
    alice_wins = np.sum(alice_heads > bob_heads)
    
    return alice_wins / num_trials

def analytical_solution(n):
    total_coins = 2 * n + 2
    center_event = n + 1

    prob_center = comb(total_coins, center_event) * (0.5**total_coins)
    
    return (1 + prob_center) / 2

n_values = [1, 10, 50, 100, 1000]

for n in n_values:
    print(f"--- Testing for n = {n} ---")
    
    simulated_prob = run_simulation(n)
    print(f"Simulated Probability: {simulated_prob:.6f}")
    
    exact_prob = analytical_solution(n)
    print(f"Exact Probability:     {exact_prob:.6f}")
    print("-" * 20 + "\n")