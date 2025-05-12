import sys
import re
from collections import defaultdict
#import time

#start_time = time.time()
file = sys.argv[1]

f = open(file, "r")
rulesmap = defaultdict(list)
total, total2 = 0, 0
for line in f:
    if "|" in line:
        n1, n2 = map(int, line.split("|"))
        rulesmap[n1].append(n2)
    if "," in line:
        nums = list(map(int, line.split(",")))
        if all(nums[i] in rulesmap[nums[i-1]] for i in range(1, len(nums))):
            total += nums[len(nums)//2]
        orignums = nums[:]
        badone = True
        while badone:
            badone = False
            for i in range(1, len(nums)):
                if not nums[i] in rulesmap[nums[i-1]]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
                    badone = True
        if orignums != nums:
            total2 += nums[len(nums)//2]
print(total)
print(total2)
print(rulesmap)