import sys
import re
#import time

#start_time = time.time()
file = sys.argv[1]

f = open(file, "r")

cons = [a.strip().split('-') for a in f] # connection + used
#print(cons)

triplets = []

for i, c in enumerate(cons):
    x,y = c
    x_cands = []
    y_cands = []
    for j in range(i + 1, len(cons)):
        c_x, c_y = cons[j]
        if x == c_x:
            if c_y in y_cands:
                triplets.append([x, y, c_y])
            else:
                x_cands.append(c_y)
        if x == c_y:
            if c_x in y_cands:
                triplets.append([x, y, c_x])
            else:
                x_cands.append(c_x)
        if y == c_x:
            if c_y in x_cands:
                triplets.append([x, y, c_y])
            else:
                y_cands.append(c_y)
        if y == c_y:
            if c_x in x_cands:
                triplets.append([x, y, c_x])
            else:
                y_cands.append(c_x)

res = []
for t in triplets:
    ap = False
    for a in t:
        if a.startswith("t"):
            ap = True
            break
    if ap:
        res.append(t)
print(len(res))
