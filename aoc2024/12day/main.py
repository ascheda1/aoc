import sys
import re
from collections import Counter
#import time

#start_time = time.time()
file = sys.argv[1]

f = open(file, "r")


def calculate_fence_price():
    total_price = 0
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                area, perimeter = dfs(r, c, grid[r][c])
                total_price += area * perimeter
    return total_price

#in_bounds
def in_b(r, c):
        return 0 <= r < rows and 0 <= c < cols

def check_surroundings(x, y):
    if not in_b(x,y):
        return
    #type
    t = grid[x][y]
    sub_g = [[grid[i][j] if in_b(i,j) else "A" for i in range(-1,2)] for j in range(-1,2)]
    print(sub_g)

def tag_side(x,y,dx,dy,plant_type):
    area = 0
    stack = []
    dirs = []
    if dir.index((dx, dy)) < 2:
        dirs.append(dir[2])
        dirs.append(dir[3])
    else:
        dirs.append(dir[0])
        dirs.append(dir[1])

    for dx_, dy_ in dirs:
        x_f, y_f = x, y
        visited[x_f][y_f] = False
        fence_len = 0
        while in_b(x_f, y_f) and grid[x_f][y_f] == plant_type and (not in_b(x_f + dx, y_f + dy) or grid[x_f + dx][y_f + dy] != plant_type):
            # fence spot
            # fence_x, fence_y = x_f + dx, y_f + dy
            fence_len+=1
            #if visited[x_f][y_f]:
            #    break
            if visited[x_f][y_f] == True:
                area += 1
            visited[x_f][y_f] = True
            stack.append((x_f, y_f))
            x_f, y_f = x_f + dx_, y_f + dy_

    new_stack = []
    for x,y in stack:
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if in_b(nx, ny) and grid[nx][ny] == plant_type:
                if not visited[nx][ny]:
                    new_stack.append((nx, ny))
    print(plant_type, area, dirs, stack, fence_len)
    for a in visited:
        print(a)
    return stack, area

def dfs(r, c, plant_type):
    stack = [(r, c)]
    area = 0
    perimeter = 0

    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue
        visited[x][y] = True
        area += 1
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if in_b(nx, ny) and grid[nx][ny] == plant_type:
                if not visited[nx][ny]:
                    stack.append((nx, ny))
            else:
                # tag side
                #new_stack, area_add = tag_side(x,y,dx,dy,plant_type)
                #area += area_add
                #for a in new_stack:
                #    stack.append(a)
                perimeter += 1
    #print(plant_type, perimeter, area)
    return area, perimeter

def calculate_new_fence_price(grid):
    rows, cols = len(grid), len(grid[0])
    visited_cells = [[False for _ in range(cols)] for _ in range(rows)]

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, plant_type):
        stack = [(r, c)]
        area = 0
        sides = 0

        while stack:
            x, y = stack.pop()
            if visited_cells[x][y]:
                continue
            visited_cells[x][y] = True
            area += 1

            # Check all 4 sides
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                # Out of bounds or different plant type -> external edge
                if not in_bounds(nx, ny) or grid[nx][ny] != plant_type:
                    sides += 1
                elif not visited_cells[nx][ny]:
                    # Same region, add to stack for DFS
                    stack.append((nx, ny))
        return area, sides

    total_price = 0
    for r in range(rows):
        for c in range(cols):
            if not visited_cells[r][c]:
                area, sides = dfs(r, c, grid[r][c])
                print(f"Region {grid[r][c]}: Area = {area}, Sides = {sides}, Price = {area * sides}")
                total_price += area * sides

    return total_price

# Example usage:
grid = [a.strip() for a in f]
rows, cols = len(grid), len(grid[0])
visited = [[False for i in range(cols)] for j in range(rows)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#print(calculate_fence_price()) 
print(calculate_new_fence_price(grid))
