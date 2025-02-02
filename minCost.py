def canMove(a, b, c, d):
    if 0<=a<=c and 0<=b<=d:
        return True
    return False

def changeMove(prev, x, y, row, col):
    if prev == 1 and y>col:
        prev = 3
        y-=1
    elif prev == 2 and y<0:
        prev = 3
        y+=1
    elif prev == 3 and x>row:
        prev = 1
        x-=1
    elif prev == 4 and x<0:
        prev = 1
        x+=1
    return prev, x, y
        

def minCost(grid):
    col = len(grid[0]) - 1
    row = len(grid) - 1
    
    cost = 0
    FLAG = True
    x, y = 0, 0
    curr = [x, y]
    target = [row, col]
    prev = 0
    
    while FLAG:
     if canMove(x, y, col, row):
         prev = grid[x][y]
         print(f'Present Location: ({x}, {y})')
         if grid[x][y] == 1:
             print('Move RIGHT!')
             y+=1
             print(f'Present Location: ({x}, {y})\n')
         elif grid[x][y] == 2:
             print('Move LEFT')
             y-=1
             print(f'Present Location: ({x}, {y})\n')
         elif grid[x][y]==3:
             print('Move DOWN')
             x+=1
             print(f'Present Location: ({x}, {y})\n')
         elif grid[x][y]==4:
             print('Move UP')
             x-=1
             print(f'Present Location: ({x}, {y})\n')
     elif [x, y] == target:
         FLAG = False
     else:
         print(f'Current Value: {x} {y}')
         prev, x, y = changeMove(prev, x, y, row, col)
         cost += 1
         print(f'New Value: {prev} {x} {y} {cost}')
         gnext = prev
         break
    return cost         

x = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
minCost(x)
