from collections import deque

def calculateDistances(grid):
    ROWS, COLS = len(grid), len(grid[0])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque()

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                queue.append((r, c))
                grid[r][c] = 0 
            else:
                grid[r][c] = -1
    
    while queue:
        x, y = queue.popleft()
        for dr, dc in directions:
            nx, ny = x + dr, y + dc
            if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == -1:
                grid[nx][ny] = grid[x][y] + 1  
                queue.append((nx, ny))         
    
    return grid

