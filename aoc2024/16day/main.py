import sys
import re
import heapq
import numpy as np
#import time

#start_time = time.time()
file = sys.argv[1]
f = open(file, "r")



maze = [[c for c in l.strip()] for l in f]

# E, W, N, S
dirs = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
rot_order = ['N', 'E', 'S', 'W']

start = None
end = None

for i, row in enumerate(maze):
    for j, cell in enumerate(row):
        if cell == 'S':
            start = (i, j, 'E')  # Start facing East
        elif cell == 'E':
            end = (i, j)

def a_star(maze, start, end):
    rows, cols = len(maze), len(maze[0])

    def heuristic(x, y):
        return abs(x - end[0]) + abs(y - end[1])

    # Priority queue (min-heap) and cost map
    pq = []
    heapq.heappush(pq, (0, 0, start, []))  # (total_cost, g_cost, (x, y, direction), path)
    cost_map = {}

    best_paths = []
    best_cost = float('inf')

    while pq:
        total_cost, g_cost, (x, y, direction), path = heapq.heappop(pq)

        # Goal check
        if (x, y) == end:
            if g_cost < best_cost:
                best_cost = g_cost
                best_paths = [path + [(x, y)]]
            elif g_cost == best_cost:
                best_paths.append(path + [(x, y)])
            continue


        state = (x, y, direction)
        if state in cost_map and g_cost > cost_map[state]:
            continue
        cost_map[state] = g_cost 

        dx, dy = dirs[direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
            heapq.heappush(pq, (g_cost + 1 + heuristic(nx, ny), g_cost + 1, (nx, ny, direction), path + [(x, y)]))

        curr_idx = rot_order.index(direction)
        for delta, cost in [(1, 1000), (-1, 1000)]:
            new_direction = rot_order[(curr_idx + delta) % 4]
            heapq.heappush(pq, (g_cost + cost + heuristic(x, y), g_cost + cost, (x, y, new_direction), path + [(x, y)]))

    sit_places = []

    for path in best_paths:
        for x, y in path:
            if [x,y] not in sit_places:
                sit_places.append([x,y])
    print(len(sit_places))
    return best_paths

# Mark the best paths on the maze
def mark_best_paths(maze, best_paths):
    n = 0
    maze_marked = [list(row) for row in maze]
    for path in best_paths:
        for x, y in path:
            if maze_marked[x][y] == '.':
                maze_marked[x][y] = 'O'
                n+=1
    print(n+2)
    return ["".join(row) for row in maze_marked]

# Run the algorithm
best_paths = a_star(maze, start, end)
marked_maze = mark_best_paths(maze, best_paths)
#for r in marked_maze:
#    print(r)
