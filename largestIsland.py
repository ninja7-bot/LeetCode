grid = [[1,0],
        [0,1]]
"""
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            area = grid[r][c]
            grid[r][c] = 0
            for dX,dY in DIRECTIONS:
                nR, nC = r + dX, c + dY
                if(0 <= nR < ROWS and 0 <= nC < COLS and grid[nR][nC]>=1):
                    area+=dfs(nR,nC)
            return area
        
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = ((0,1),(1,0),(-1,0),(0,-1))
        res = 0

        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j]>0):
                    res = max(res, dfs(i,j))
        return res
1. Source
2. Source pe DFS perform karu.
3. DFS se find karu the number of 1s.
4. Jaise hi 0 encounter ho then usko 1 mai flip karke result return kardo.
5. If 0 encounter na ho then it is full of 1s.
"""

def largestIsland(grid):
    n = len(grid)
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def dfs(r, c, visited):
        if not (0 <= r < n and 0 <= c < n) or (r, c) in visited or grid[r][c] == 0:
            return 0
        visited.add((r, c))
        size = 1
        for dx, dy in directions:
            size += dfs(r + dx, c + dy, visited)
        return size

    max_island = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                visited = set()
                max_island = max(max_island, dfs(i, j, visited))

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                visited = set()
                grid[i][j] = 1
                max_island = max(max_island, dfs(i, j, visited))
                grid[i][j] = 0

    return max_island

             


print(largestIsland(grid))
