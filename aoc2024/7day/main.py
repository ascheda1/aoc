import sys
import re
#import time

concatenations = []

def sum_options(result, nums, current_res = 0, idx = 1):
    #print(current_res)
    if idx == len(nums):
        if result == current_res:
            return 1
        else:
            return 0
    return sum_options(result, nums, current_res * nums[idx], idx+1) + sum_options(result, nums, current_res + nums[idx], idx + 1) + sum_options(result, nums, int(str(current_res) + str(nums[idx])), idx + 1)
    
def generate_concatenations(nums, idx = 0):
    if idx == len(nums) - 1:
        concatenations.append(nums)
        return
    new_arr = []
    # do cont
    for i in range(0, idx):
        new_arr.append(nums[i])
    new_arr.append(int(str(nums[idx]) + str(nums[idx+1])))
    for i in range(idx+2, len(nums)):
        new_arr.append(nums[i])
    #dont do cont
    generate_concatenations(new_arr, 0)
    generate_concatenations(nums, idx + 1)

#start_time = time.time()
file = sys.argv[1]

f = open(file, "r")

sum = 0
for line in f:
    l = line.split(":")
    result = int(l[0])
    nums_s = l[1].strip().split(" ")
    nums = []
    for n in nums_s:
        nums.append(int(n))

    #concatenations = []
    #generate_concatenations(nums)
    #print(concatenations)
    if sum_options(result, nums, nums[0]) > 0:
        sum += result 

print(sum)