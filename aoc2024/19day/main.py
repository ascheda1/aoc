import sys
import re
#import time

#start_time = time.time()
file = sys.argv[1]

f = open(file, "r")


def count_possible_designs(towels, designs):
    def can_form_design(design, towel_set):
        n = len(design)
        # DP array to store whether a prefix of `design` can be formed
        dp = [False] * (n + 1)
        dp[0] = True  # Empty prefix can always be formed

        for i in range(1, n + 1):
            for towel in towel_set:
                towel_len = len(towel)
                # Check if the current towel matches the end of the current prefix
                if i >= towel_len and design[i - towel_len:i] == towel and dp[i - towel_len]:
                    dp[i] = True
                    break  # No need to check further if this prefix is valid
        
        return dp[n]

    # Convert the towels into a set for faster lookup
    towel_set = set(towels)
    possible_count = 0

    for design in designs:
        if can_form_design(design, towel_set):
            possible_count += 1

    return possible_count


def count_all_arrangements(towels, designs):
    def count_ways(design, towel_set):
        n = len(design)
        # DP array where dp[i] stores the number of ways to form design[:i]
        dp = [0] * (n + 1)
        dp[0] = 1  # There's 1 way to form an empty prefix (do nothing)

        for i in range(1, n + 1):
            for towel in towel_set:
                towel_len = len(towel)
                # Check if the current towel matches the end of the current prefix
                if i >= towel_len and design[i - towel_len:i] == towel:
                    dp[i] += dp[i - towel_len]
        
        return dp[n]

    # Convert towels to a set for faster lookup
    towel_set = set(towels)
    total_arrangements = 0

    # Sum the ways for all designs
    for design in designs:
        total_arrangements += count_ways(design, towel_set)

    return total_arrangements


designs = []
for l in f:
    if "," in l:
        towels = l.strip().split(", ")
    else:
        designs.append(l.strip())

print(towels)
print(designs)

# Output: Count of possible designs
result = count_possible_designs(towels, designs)
print(f"Number of possible designs: {result}")
result2 = count_all_arrangements(towels, designs)
print(result2)