import sys
import re
from operator import mul

file = sys.argv[1]

f = open(file, "r")
input = f.read()
lines = input.split('\n')

symbol_regex = r'[^.\d]'
symbol_adjacent = set()
for i, line in enumerate(lines):
    for m in re.finditer(symbol_regex, line):
        j = m.start()
        symbol_adjacent |= {(r, c) for r in range(i-1, i+2) for c in range(j-1, j+2)}

number_regex = r'\d+'
part_num_sum = 0
for i, line in enumerate(lines):
    for m in re.finditer(number_regex, line):
        if any((i, j) in symbol_adjacent for j in range(*m.span())):
            part_num_sum += int(m.group())
            
print(part_num_sum)