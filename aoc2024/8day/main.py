import sys
import re
#import time

#start_time = time.time()
file = sys.argv[1]

f = open(file, "r")
grid = f.read().splitlines()
bounds = len(grid[0]) + len(grid) * 1j

def find_in_grid(grid, c):
    idx = []
    y = 1
    for line in grid:
        l = list(line)
        for x in range(len(l)):
            if l[x] == c:
                idx.append(x + 1 + y * 1j)
        y += 1
    return idx

antenas = set(i for i in "".join(grid))
antenas.remove(".")

res1 = set()
res2 = set()
for a in antenas:
    idx = find_in_grid(grid,a)
    for i1 in idx:
        for i2 in idx:
            vec = i1 + (i1-i2)
            if i1!=i2 and 0<vec.real<=bounds.real and 0<vec.imag<=bounds.imag:
                res1.add(vec)
            temp = i1  
            vec = i1 - i2
            if vec != 0j:
                while 0<temp.real<=bounds.real and 0<temp.imag<=bounds.imag:
                    res2.add(temp)
                    temp+=vec
print(len(res1))
print(len(res2))