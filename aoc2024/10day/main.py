import sys
import re
from collections import deque
#import time

#start_time = time.time()
file = sys.argv[1]

f = open(file, "r")
map_str = ""
for l in f:
    map_str += l

def parse_map(map_str):
    return [list(map(int, line)) for line in map_str.strip().split("\n")]

def find_trailheads(grid):
    trailheads = []
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == 0:
                trailheads.append((r, c))
    return trailheads

def calculate_score(grid, trailhead):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    queue = deque([trailhead])
    reachable_nines = set()
    count_approaches = 0
    while queue:
        r, c = queue.popleft()
        
        # part 1
        #if (r, c) in visited:
        #    continue
        visited.add((r, c))
        
        if grid[r][c] == 9:
            reachable_nines.add((r, c))
            count_approaches += 1
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == grid[r][c] + 1:
                    queue.append((nr, nc))
    
    return count_approaches
    return len(reachable_nines)

def sum_trailhead_scores(map_str):
    grid = parse_map(map_str)
    trailheads = find_trailheads(grid)
    return sum(calculate_score(grid, trailhead) for trailhead in trailheads)

print(sum_trailhead_scores(map_str))
