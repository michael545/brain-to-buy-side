"""
A deck has 35 red cards and 65 black cards, shuffled randomly.
Cards are drawn one by one without replacement until 
all cards of one color are exhausted.
What is the expected number of cards remaining in the deck at that point?
"""
import numpy as np
import matplotlib.pyplot as plt

def simulate_cards_remaining():
    red_cards = 35
    black_cards = 65
    total_cards = red_cards + black_cards
    
    # deck: 0 = red, 1 = black
    deck = np.concatenate([np.zeros(red_cards), np.ones(black_cards)])
    np.random.shuffle(deck)
    
    red_count = red_cards
    black_count = black_cards
    
    for i, card in enumerate(deck):
        if card == 0:  # red card drawn
            red_count -= 1
        else:  # black card drawn
            black_count -= 1
            
        if red_count == 0 or black_count == 0:
            return total_cards - (i + 1)
    
    return 0

n_simulations = 100000
remaining_cards = [simulate_cards_remaining() for _ in range(n_simulations)]
sim_mean = np.mean(remaining_cards)

# Theoretical: E[remaining] = |R-B| = |35-65| = 30
theoretical_mean = abs(35 - 65)

plt.figure(figsize=(10, 6))
plt.hist(remaining_cards, bins=range(0, max(remaining_cards) + 2), 
         density=True, alpha=0.7, color='brown', edgecolor='black')
plt.axvline(sim_mean, color='red', linestyle='--', linewidth=2, 
            label=f'Simulated Mean: {sim_mean:.4f}')
plt.axvline(theoretical_mean, color='blue', linestyle=':', linewidth=2, 
            label=f'Theoretical Mean: {theoretical_mean}')
plt.xlabel('Cards Remaining')
plt.ylabel('Density')
plt.title('Distribution of Cards Remaining When One Color Exhausted')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print(f"Expected cards remaining: {sim_mean:.6f}")
print(f"Theoretical value: {theoretical_mean}")
