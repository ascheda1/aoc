import sys
import re
#import time

#start_time = time.time()
file = sys.argv[1]

f = open(file, "r")
corrupted_memory = ""

for line in f:
    corrupted_memory += line

result_sum = 0
enabled = True
matches = re.finditer(r"don't\(\)|do\(\)|mul\((\d+),(\d+)\)",corrupted_memory)
for match in matches:
    if match[0] and match[1]: 
        if enabled:
            result_sum += int(match.group(1)) * int(match.group(2))
    elif "do()" in match[0]: 
        enabled = True
    elif "don" in match[0]: 
        enabled = False

print(result_sum)