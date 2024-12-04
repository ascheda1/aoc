import sys
import time

start_time = time.time()
file = sys.argv[1]

f = open(file, "r")

def safe_check(ints): 
    increasing = False
    if ints[0] - ints[1] < 0:
        increasing = True
    safe_repo = True
    for i in range(1, len(ints)):
        if abs(ints[i] - ints[i - 1]) > 3 or ints[i] - ints[i - 1] == 0:
            safe_repo = False
            break 

        if increasing and ints[i] < ints[i - 1]:
            safe_repo = False
            break
        if not increasing and ints[i] > ints[i - 1]:
            safe_repo = False
            break
    return safe_repo

safe_repos = 0
for line in f:
    n = line.split(" ")
    ints = []
    for s in n:
        ints.append(int(s.strip()))

    is_safe = False
    if not safe_check(ints):
        for i in range(0, len(ints)):
            extra_arr = list(ints)
            extra_arr.pop(i)
            if safe_check(extra_arr):
                safe_repos += 1
                break
    else:
        safe_repos += 1
    


print("Answer:", safe_repos)
print("--- %s miliseconds ---" % ((time.time() - start_time) * 1000))