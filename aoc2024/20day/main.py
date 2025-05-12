import sys
import re
import heapq
from copy import copy, deepcopy
from collections import Counter
#import time

#start_time = time.time()

def get_neighbors(pos, grid):
    """Return valid neighbors for the current position."""
    x, y = pos
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    valid_neighbors = []
    
    for nx, ny in neighbors:
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (grid[nx][ny] == '.' or grid[nx][ny] == 'S' or grid[nx][ny] == 'E'):
            valid_neighbors.append((nx, ny))

    return valid_neighbors

def heuristic(a, b):
    """Calculate the Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal, original_price):
    """Perform the A* search on the grid."""
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        #if g_score[current] + cheat_limit > original_price:
        #    continue
        for neighbor in get_neighbors(current, grid):
            tentative_g_score = g_score[current] + 1
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                current_heuristic = heuristic(neighbor, goal)
                f_score[neighbor] = tentative_g_score + current_heuristic
                #if current_heuristic + g_score[neighbor] + cheat_limit > original_price:
                #    continue
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path found

def clean_up_grid(grid, pos, radius = 20):
    x,y = pos
    for i, arr in enumerate(grid):
        for j, c in enumerate(arr):
            if abs(i - x) + abs(j - y) < radius:
                grid[i][j] = '.'


def print_grid(grid):
    print(["".join(row) for row in grid])

def mark_best_paths(maze, best_path):
    maze_marked = [list(row) for row in maze]
    for x,y in best_path:
        if maze_marked[x][y] == '.':
            maze_marked[x][y] = 'O'

    for row in maze_marked:
        print("".join(row))

file = sys.argv[1]

f = open(file, "r")

grid = [[c for c in l.strip()] for l in f]
cheat_limit = 50
candidates = []
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if grid[i][j] == '#':
            candidates.append((i,j))
        if cell == 'S':
            start = (i, j)  # Start facing East
        elif cell == 'E':
            end = (i, j)

price = len(a_star(grid, start, end, sys.maxsize))
print(price)
cheats = [0] * price

for cand in candidates:
    x,y = cand
    cheat_grid = deepcopy(grid)
    extra_grid = deepcopy(grid)
    extra_grid[x][y] = '.'
    # clean up grid
    clean_up_grid(cheat_grid, (x,y), 19)
    #print_grid(cheat_grid)
    path_to_cand = a_star(extra_grid, start, cand, price) 
    path_to_end = a_star(cheat_grid, cand, end, price)
    if path_to_cand == None or path_to_end == None:
        continue
    mark_best_paths(cheat_grid, path_to_cand + path_to_end)
    cheat_price = len(path_to_cand + path_to_end)
    print(cheat_price)
    if cheat_price < price:
        cheats[price - cheat_price] += 1
for i, n in enumerate(cheats):
    if i < cheat_limit or n == 0:
        continue
    print('There are', n, 'cheats that save', i, 'picoseconds.')

print(sum(cheats[cheat_limit:len(cheats)]))