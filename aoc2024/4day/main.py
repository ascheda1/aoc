import sys
import re
#import time

#start_time = time.time()
file = sys.argv[1]

f = open(file, "r")

grid = []

for line in f:
    grid.append(line.strip())

target_word = "XMAS"

directions = [
    (0, 1),  
    (1, 0),  
    (1, 1),  
    (1, -1), 
    (0, -1), 
    (-1, 0), 
    (-1, -1),
    (-1, 1)  
]

def count_word_occurrences(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_length = len(word)
    count = 0
    
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                match = True
                for i in range(word_length):
                    nr, nc = r + dr * i, c + dc * i
                    if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != word[i]:
                        match = False
                        break
                if match:
                    count += 1
    return count

print(count_word_occurrences(grid, target_word))

def is_mas(seq):
    return seq == "MAS" or seq == "SAM"

def count_x_mas_with_a_center(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    for r in range(1, rows - 1): 
        for c in range(1, cols - 1):
            if grid[r][c] == "A":                
                word_one, word_two = "", ""
                word_one += grid[r - 1][c - 1] + "A" + grid[r + 1][c + 1]
                word_two += grid[r - 1][c + 1] + "A" + grid[r + 1][c - 1]
                if is_mas(word_one) and is_mas(word_two):
                    count += 1

    return count

print(count_x_mas_with_a_center(grid))
