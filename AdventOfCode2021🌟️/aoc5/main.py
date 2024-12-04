import numpy as np
from dataclasses import dataclass

@dataclass
class Point:
    x1: int
    y1: int
    x2: int
    y2: int

data = list(open('my_in.txt', 'r').read().split('\n'))
data.pop()
Points = []
xMax = yMax = 0
for d in data:
    d = d.split(' -> ')
    x1, y1 = [int(i) for i in (d[0].split(','))]
    x2, y2 = [int(i) for i in (d[1].split(','))]
    Points.append(Point(x1, y1, x2, y2))
    xMax = max(x1, x2, xMax)
    yMax = max(y1, y2, yMax)

field = [[0] * (yMax+1) for _ in range(xMax+1)]
for p in Points:
    xc,yc = p.x1, p.y1
    hxdir = p.x2 - p.x1
    hydir = p.y2 - p.y1
    xdir = 0 if hxdir == 0 else int(hxdir/abs(hxdir))
    ydir = 0 if hydir == 0 else int(hydir/abs(hydir))
    #if xdir != 0 and ydir != 0: continue
    while xc != p.x2 or yc != p.y2:
        field[xc][yc] += 1
        xc += xdir
        yc += ydir
    field[xc][yc]+=1

print((np.asarray(field) > 1).sum())
