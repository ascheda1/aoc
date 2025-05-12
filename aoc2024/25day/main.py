import sys
import re
import copy
#import time

#start_time = time.time()
file = sys.argv[1]

f = open(file, "r")

keys = []
locks = []

key = False
new_key = True
kl = [-1, -1, -1, -1, -1] # key / lock
for l in f:
    if not l.strip():
        app = copy.deepcopy(kl)
        keys.append(app) if key else locks.append(app)
        new_key = True
        continue

    if new_key:
        new_key = False
        key = True if l[0] == '#' else False
        #comp_char = '#' if key else '.'
        kl = [-1, -1, -1, -1, -1]
    for i, c in enumerate(l.strip()):
        if c == '#':
            kl[i]+=1

fit = 0
for key in keys:
    for lock in locks:
        result = [a + b for a, b in zip(key, lock)]
        print(key, lock, result)
        if all(val <= 5 for val in result):
            fit+=1

print(fit)