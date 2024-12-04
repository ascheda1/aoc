import sys

file = sys.argv[1]

f = open(file, "r")

left = []
right = []
for line in f:
    n = line.split("   ")
    left.append(int(n[0].strip()))
    right.append(int(n[1].strip()))

left.sort()
right.sort()
 
res = [abs(x-y) for x,y in zip(left, right)]

print(sum(res))

res = 0
for n in left:
    c = right.count(n)
    res += n * c

print(res)