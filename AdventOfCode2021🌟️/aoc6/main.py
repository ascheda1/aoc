import numpy as np
from dataclasses import dataclass
from collections import deque

data = [int(i) for i in list(open('in.txt', 'r').read().split(','))]

day_count = 256
fishes = deque([0 for i in range(0, 9)])

for i in data:
    fishes[i]+=1

for day in range(0, day_count):
    fishes.rotate(-1)
    fishes[6] += fishes[8]

total_fish = sum(fishes)
print(total_fish)
