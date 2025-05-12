def get_neighbors(x, y, n, m):
    """Get the valid neighbors of a cell (x, y) in the grid."""
    neighbors = []
    if x > 0: neighbors.append((x - 1, y))  # Up
    if x < n - 1: neighbors.append((x + 1, y))  # Down
    if y > 0: neighbors.append((x, y - 1))  # Left
    if y < m - 1: neighbors.append((x, y + 1))  # Right
    return neighbors

def dfs(grid, x, y, plant_type, visited):
    """DFS to find all cells in the same region."""
    stack = [(x, y)]
    region_cells = []
    visited[x][y] = True
    
    while stack:
        cx, cy = stack.pop()
        region_cells.append((cx, cy))
        
        for nx, ny in get_neighbors(cx, cy, len(grid), len(grid[0])):
            if not visited[nx][ny] and grid[nx][ny] == plant_type:
                visited[nx][ny] = True
                stack.append((nx, ny))
    
    return region_cells

def count_sides(grid, region_cells, n, m):
    """Count the number of sides for the given region."""
    sides = 0
    for x, y in region_cells:
        # Check all 4 possible sides of each cell
        for nx, ny in get_neighbors(x, y, n, m):
            # If the neighbor is out of bounds or a different plant type, it's a side
            if grid[nx][ny] != grid[x][y]:  
                sides += 1
        # Edge of the grid (if it's a boundary cell, count it as a side)
        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            sides += 1
    return sides

def calculate_total_price(grid):
    """Calculate the total price of fencing all regions."""
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]
    total_price = 0
    
    # Go through each cell and find unvisited regions
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                plant_type = grid[i][j]
                # Find the region for this plant type
                region_cells = dfs(grid, i, j, plant_type, visited)
                # Calculate area and sides
                area = len(region_cells)
                sides = count_sides(grid, region_cells, n, m)
                # Calculate price for this region
                total_price += area * sides
    
    return total_price

# Example map
grid = [
    ['A', 'A', 'A', 'A'],
    ['B', 'B', 'C', 'D'],
    ['B', 'B', 'C', 'C'],
    ['E', 'E', 'E', 'C']
]

# Calculate the total price
total_price = calculate_total_price(grid)
print("Total price:", total_price)
