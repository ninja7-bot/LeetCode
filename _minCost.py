from collections import deque

def minCost(grid):
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # RIGHT, LEFT, DOWN, UP
    cost = [[float('inf')] * n for _ in range(m)]  # Cost grid
    cost[0][0] = 0  # Starting point has zero cost
    queue = deque([(0, 0)])  # BFS queue

    while queue:
        x, y = queue.popleft()

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:  # Valid move
                new_cost = cost[x][y] + (1 if grid[x][y] != i + 1 else 0)  # Add cost if direction changes
                if new_cost < cost[nx][ny]:
                    cost[nx][ny] = new_cost
                    if grid[x][y] == i + 1:  # Follow the current direction
                        queue.appendleft((nx, ny))
                    else:  # Change direction
                        queue.append((nx, ny))

    return cost[m - 1][n - 1]  # Minimum cost to reach bottom-right corner

# Example grid
grid = [[1, 1, 1, 1], 
        [2, 2, 2, 2], 
        [1, 1, 1, 1], 
        [2, 2, 2, 2]]

print(minCost(grid))
