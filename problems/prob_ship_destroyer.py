import numpy as np

def simulate_ship_problem(n_simulations: int = 2_000_000) -> float:
    n_bombs = 4
    grid_size = 4
    
    bomb_rows = np.random.randint(0, grid_size, size=(n_simulations, n_bombs))
    bomb_cols = np.random.randint(0, grid_size, size=(n_simulations, n_bombs))
    all_rows_hit = np.array([len(np.unique(bomb_rows[i])) 
                             for i in range(n_simulations)]) == grid_size

    all_cols_hit = np.array([len(np.unique(bomb_cols[i])) 
                             for i in range(n_simulations)]) == grid_size

    #success if all_rows_hit OR all_cols_hit
    successes = np.logical_or(all_rows_hit, all_cols_hit)
    # success array (mean of 1s and 0s)
    return np.mean(successes)

if __name__ == "__main__":
    
    estimated_probability = simulate_ship_problem(n_simulations=5_000_000)
    
    analytical_prob = 11712 / (16**4)

    print(f"Should be {analytical_prob:.6f} fract: (11712 / 65536)")
    print(f"MC setimate(5mil sims): {estimated_probability:.6f}")
    print(f"Delta: {abs(estimated_probability - analytical_prob):.6f}")