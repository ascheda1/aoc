import sys
import re
import heapq
#import time

#start_time = time.time()

def get_neighbors(pos, grid):
    """Return valid neighbors for the current position."""
    x, y = pos
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    valid_neighbors = []
    
    for nx, ny in neighbors:
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '.':
            valid_neighbors.append((nx, ny))

    return valid_neighbors

def heuristic(a, b):
    """Calculate the Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
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

        for neighbor in get_neighbors(current, grid):
            tentative_g_score = g_score[current] + 1
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path found

def display_path(grid, path = None):
    """Print the grid with the path marked."""
    if path != None:
        for x, y in path:
            grid[x][y] = 'o'

    for row in grid:
        print(''.join(row))

file = sys.argv[1]

f = open(file, "r")

coords = []
for l in f:
    coords.append([int(i) for i in l.strip().split(",")])

size = 6
limit = 12

grid = [["." for i in range(size + 1)] for j in range(size + 1)]
for e,coord in enumerate(coords):
    y,x = coord
    if e == limit:
        break
    grid[x][y] = "#"
#print(grid)
for i in range(limit, len(coords)):
    y,x = coords[i]
    grid[x][y] = "#"
    path = a_star(grid, (0,0), (size, size))
    if path == None:
        print(x,y)
        display_path(grid, path)
        break