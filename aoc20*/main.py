import sys
import time

start_time = time.time()
file = sys.argv[1]

f = open(file, "r")

floor = 0
counter = 0
for l in f:
    for c in l:
        if c == '(':
            floor+=1
        else:
            floor -=1
        counter+=1
        if floor == -1:
            break

print(counter)
print("--- %s seconds ---" % (time.time() - start_time))