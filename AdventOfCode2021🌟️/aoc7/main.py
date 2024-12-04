import numpy as np
from dataclasses import dataclass
import sys

@dataclass
class Point:
    x1: int
    y1: int
    x2: int
    y2: int

def advancedcost(i):
    ret = 0
    for j in range(i+1):
        ret+=j
    return ret

def fuelcount(data, position):
    fuel = 0
    for d in data:
        fuel+=advancedcost(abs(d-position))
    return fuel

data = [int(i) for i in list(open('in.txt', 'r').read().split(','))]
#print(int(round(sum(data)/len(data))))
#print(fuelcount(data, int(round(sum(data)/len(data)))))

bestfuel = sys.maxsize
for i in range(np.min(data), np.max(data)):
    fuel = fuelcount(data, i)
    if fuel < bestfuel:
        bestfuel = fuel

print(bestfuel)
