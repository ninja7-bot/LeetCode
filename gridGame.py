"""
You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c] represents the number of points at position (r, c) on the matrix.
Two robots are playing a game on this matrix.

Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot may only move to the right ((r, c) to (r, c + 1)) or down ((r, c)
to (r + 1, c)).

At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells on its path.
For all cells (r, c) traversed on the path, grid[r][c] is set to 0. Then, the second robot moves from (0, 0) to (1, n-1), collecting
the points on its path. Note that their paths may intersect with one another.

The first robot wants to minimize the number of points collected by the second robot. In contrast, the second robot wants to maximize
the number of points it collects. If both robots play optimally, return the number of points collected by the second robot.
"""

def gridGame(grid):
    scores = []
    ROWS = 2
    COLS = len(grid[0])

    for r in range(1):
        for c in range(COLS):
            if c == COLS - 1:
                _scores = [sum(grid[0][c:]) + grid[1][COLS-1], sum(grid[1][c:])]
            else:
                _scores = [sum(grid[0][c:]) + grid[1][COLS-1], grid[r][c] + sum(grid[1][c:])]
            scores.append(_scores)
            
    ROW = 0
    c = 0
    while c != COLS:
        if scores[c][0] >= scores[c][1] and ROW == 0:
            if c == COLS - 1:
                grid[0][c] = 0
                ROW = 1
            else:
                grid[0][c] = 0
                c+=1
        elif scores[c][0] <= scores[c][1] and ROW == 0:
            ROW = 1
            grid[0][c] = 0
            continue
        elif ROW == 1:
            grid[1][c] = 0
            c += 1
        elif c == COLS - 1:
            if ROW == 0:
                grid[0][c] = 0
                ROW = 1
            else:
                grid[ROW][c] = 0
    print(grid)                
    score = 0
    ROW = 0
    C = 0
    while C != COLS:
        A = sum(grid[0][C:]) + grid[1][COLS-1]
        B = grid[0][C] + sum(grid[1][C:])
        if A > B and ROW == 0:
            if C == COLS - 1:
                score += grid[0][C]
                ROW = 1
            else:
                score+=grid[0][C]
                C+=1
        elif A < B and ROW == 0:
            score+=grid[ROW][C]
            ROW = 1
        elif ROW == 1:
            score+=grid[1][C]
            C+=1
        elif C == COLS - 1 and ROW == 1:
            score += grid[1][C]
        
    return score                
        
print(gridGame([[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]))
