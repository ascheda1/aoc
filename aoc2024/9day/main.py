import sys
import re
#import time

#start_time = time.time()
file = sys.argv[1]

f = open(file, "r")
line = ""
for l in f:
    line = l

arr = []
num = 0
skip = False
for n in l:
    for i in range(int(n)):
        if skip:
            arr.append(".")
        else:
            arr.append(num)
    if skip:
        skip = False
    else:
        skip = True
        num+=1

j = len(arr) - 1
for i in range(len(arr)):
    num = arr[i]
    if num == ".":
        while arr[j] == ".":
            j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
arr = [i for i in arr if i != "."]
res = 0

for i in range(len(arr)):
    res+= i * arr[i]
print(res)



