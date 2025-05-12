import sys
import re
from collections import Counter
#import time

#start_time = time.time()
file = sys.argv[1]

f = open(file, "r")


def split_number(n):
    s = str(n)
    mid = len(s) // 2
    left, right = int(s[:mid]), int(s[mid:])
    return left, right

def blink_batch(stone_counts, memo):
    new_stone_counts = Counter()
    for stone, count in stone_counts.items():
        if stone in memo:
            results = memo[stone]
        else:
            if stone == 0:
                results = [1]
            elif len(str(stone)) % 2 == 0:
                left, right = split_number(stone)
                results = [left, right]
            else:
                results = [stone * 2024]

            memo[stone] = results

        for result in results:
            new_stone_counts[result] += count

    return new_stone_counts

def simulate_blinks(initial_stones, num_blinks):
    stone_counts = Counter(initial_stones)
    memo = {}
    for _ in range(num_blinks):
        stone_counts = blink_batch(stone_counts, memo)
    return stone_counts

initial_stones = [int(a) for l in f for a in l.strip().split(" ")]
num_blinks = 75

result = simulate_blinks(initial_stones, num_blinks)
#print(f"After {num_blinks} blinks: {result}")
print(sum(result.values()))
