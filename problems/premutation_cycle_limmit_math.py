import numpy as np

def calculate_expected_value(n):
    total_sum = 0.0
    for k in range(n + 1, 2 * n + 1):
        total_sum += 1 / k
    return total_sum

# --- Main ---
ln2 = np.log(2)
print(f"theory alone\"openhimer\": {ln2:.10f}\n")

n_values = [100, 1000, 10000, 100000, 1000000]

for n in n_values:
    calculated_sum = calculate_expected_value(n)
    difference = abs(ln2 - calculated_sum)
    print(f"For n = {n:<7} -> Sum = {calculated_sum:.10f} (Delta: {difference:.10f})")