import sys
import re
from queue import Queue
#import time

#start_time = time.time()
file = sys.argv[1]

f = open(file, "r")
vals = {}
values_loaded = False
eqs = Queue()

for l in f:
    if values_loaded:
        x,op,y,arrow,out = l.strip().split(' ')
        eqs.put([x,op,y,out])
        continue
    if l in ['\n', '\r\n']:
        values_loaded = True
        continue
    val, num = l.strip().split(': ')
    vals[val] = int(num)


while not eqs.empty():
    x,op,y,out = eqs.get()
    if x not in vals or y not in vals:
        eqs.put([x,op,y,out])
        continue
    if op == "XOR":
        vals[out] = vals[x] ^ vals[y]
    elif op == "OR":
        vals[out] = vals[x] or vals[y]
    elif op == "AND":
        vals[out] = vals[x] and vals[y]


res = ""
for val in reversed(sorted(vals)):
    if 'z' in val:
        print(val, vals[val])
        res += str(vals[val])

print(res)