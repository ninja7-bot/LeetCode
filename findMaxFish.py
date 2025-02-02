grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
"""
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

    A land cell if grid[r][c] = 0, or
    A water cell containing grid[r][c] fish, if grid[r][c] > 0.

A fisher can start at any water cell (r, c) and can do the following operations any number of times:

    Catch all the fish at cell (r, c), or
    Move to any adjacent water cell.

Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.
"""
def findMaxFish(grid):
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
print(findMaxFish(grid))
"""


def findMaxFish(grid):
    ROWS, COLS = len(grid), len(grid[0])
    AREA = []
    for i in range(ROWS):
        area = 0
        for j in range(COLS):
            if grid[i][j] == 0:
                area = 0
                continue
            elif grid[i][j] > 0:
                area+=grid[i][j]

"""
































    
    
