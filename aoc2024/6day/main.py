import sys
import re
import time

def simulate_guard_path(lab_map):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_order = ['^', '>', 'v', '<']

    rows = len(lab_map)
    cols = len(lab_map[0])
    visited = set()
    guard_pos = None
    guard_dir = None
    
    for r in range(rows):
        for c in range(cols):
            if lab_map[r][c] in directions:
                guard_pos = (r, c)
                guard_dir = lab_map[r][c]
                break
        if guard_pos:
            break
    
    while True:
        visited.add(guard_pos)
        r, c = guard_pos
        dr, dc = directions[guard_dir]
        next_pos = (r + dr, c + dc)
 
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break

        if lab_map[next_pos[0]][next_pos[1]] == '#':
            current_index = turn_order.index(guard_dir)
            guard_dir = turn_order[(current_index + 1) % 4]
        else:
            guard_pos = next_pos
    
    return visited

def simulate_guard_path_with_obstacle(lab_map, obstacle=None):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_order = ['^', '>', 'v', '<']
    rows = len(lab_map)
    cols = len(lab_map[0])
    
    guard_pos = None
    guard_dir = None
    for r in range(rows):
        for c in range(cols):
            if lab_map[r][c] in directions:
                guard_pos = (r, c)
                guard_dir = lab_map[r][c]
                break
        if guard_pos:
            break

    if obstacle:
        lab_map[obstacle[0]][obstacle[1]] = '#'
    
    visited_states = set()
    while True:
        state = (guard_pos, guard_dir)
        if state in visited_states:
            return True 
        visited_states.add(state)
        
        r, c = guard_pos
        dr, dc = directions[guard_dir]
        next_pos = (r + dr, c + dc)
        
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break

        if lab_map[next_pos[0]][next_pos[1]] == '#':
            current_index = turn_order.index(guard_dir)
            guard_dir = turn_order[(current_index + 1) % 4]
        else:
            guard_pos = next_pos

    return False

def count_loop_positions(lab_map, visited):
    rows = len(lab_map)
    cols = len(lab_map[0])
    loop_positions = 0
    for r,c in visited:
        lab_map_copy = [row[:] for row in lab_map]
        if simulate_guard_path_with_obstacle(lab_map_copy, (r, c)):
            loop_positions += 1

    return loop_positions


start_time = time.time()
file = sys.argv[1]

f = open(file, "r")
lab_map = []
for line in f:
    lab_map.append(line.strip())

lab_map = [list(row) for row in lab_map]
visited = simulate_guard_path(lab_map)
valid_positions = count_loop_positions(lab_map, visited)
print(valid_positions)
print("--- %s miliseconds ---" % ((time.time() - start_time) * 1000))
