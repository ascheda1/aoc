import sys
import re
import heapq
from copy import copy, deepcopy
from collections import Counter
#import time

#start_time = time.time()

def simulate_secret_number(initial_secret, iterations=2000):
    MODULO = 16777216

    secret = initial_secret

    for _ in range(iterations):
        # Step 1: Multiply by 64 and XOR
        secret ^= (secret * 64)
        secret %= MODULO  # Prune

        # Step 2: Divide by 32, floor it, then XOR
        secret ^= (secret // 32)
        secret %= MODULO  # Prune

        # Step 3: Multiply by 2048 and XOR
        secret ^= (secret * 2048)
        secret %= MODULO  # Prune

    return secret

def sum_2000th_secrets(initial_secrets):
    total = 0
    for secret in initial_secrets:
        total += simulate_secret_number(secret)
    return total

# Example Input
file = sys.argv[1]

f = open(file, "r")
initial_secrets = [int(a.strip()) for a in f]

# Simulate and Output the Result
result = sum_2000th_secrets(initial_secrets)
print(f"The sum of the 2000th secret numbers is: {result}")
