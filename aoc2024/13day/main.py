import sys
import re
from collections import Counter
#import time

#start_time = time.time()
file = sys.argv[1]

f = open(file, "r")

def parse_input():
    machines = []
    with open(file, 'r') as f:
        lines = f.read().strip().split('\n\n')  # Split by blank lines
        for block in lines:
            entries = block.split('\n')
            A = tuple(map(int, entries[0].split(': ')[1].replace('X+', '').replace('Y+', '').split(', ')))
            B = tuple(map(int, entries[1].split(': ')[1].replace('X+', '').replace('Y+', '').split(', ')))
            prize = tuple(map(int, entries[2].split(': ')[1].replace('X=', '').replace('Y=', '').split(', ')))
            #prize_n = tuple([prize[0] + 10000000000000,prize[1] + 10000000000000])
            machines.append({'A': A, 'B': B, 'prize': prize})
    return machines

def solve_claw_machines(machines, max_presses=None):
    results = []

    for machine in machines:
        a, c = machine['A']
        b, d = machine['B']
        Px, Py = machine['prize']

        # Solve for x_A and x_B using the constraints
        found_solution = False
        min_cost = float('inf')

        for x_A in range(max_presses + 1 if max_presses else Px // a + 1):
            for x_B in range(max_presses + 1 if max_presses else Px // b + 1):
                if (a * x_A + b * x_B == Px) and (c * x_A + d * x_B == Py):
                    found_solution = True
                    cost = 3 * x_A + 1 * x_B
                    if cost < min_cost:
                        min_cost = cost

        if found_solution:
            results.append(min_cost)

    # Summarize results
    total_prizes_won = len(results)
    total_tokens_spent = sum(results)
    
    return total_prizes_won, total_tokens_spent

# Summarize results
print(solve_claw_machines(parse_input(), 100))
