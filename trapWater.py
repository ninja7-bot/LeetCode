def trap(height):
    LENGTH = len(height) - 1
    res = 0
    prevHeight = 0
    #nextHeight = height[1]

    for i in range(0, LENGTH+1):
        if i == 0 or i == LENGTH:
            print('\tSTATE 0\nSKIP')
            continue
#  (prevHeight < height[i] < height[i+1]) or 
        if (height[i] > height[i+1] and height[i] > prevHeight):
            print(f"\tSTATE 1: \nCurrent Amount: {res}\nCurrent Height: {height[i]} | Prev Height: {prevHeight} | Next Height: {height[i+1]}")
            prevHeight = height[i] # 1: 1, 3: 2
            print("NO RESULT CHANGE: ", res)
            print(f"Previous Height: {prevHeight}\n")
            continue
        elif height[i] < prevHeight and height[i] < height[i+1]:
            print(f"\tSTATE 2\nCurrent Amount: {res}\nCurrent Height: {height[i]} | Prev Height: {prevHeight} | Next Height: {height[i+1]}")
            print("Result: ", res)
            print(height[i+1] - height[i])
            print(height[i] - prevHeight)
            print(min(height[i+1] - height[i], abs(height[i] - prevHeight)))
            # The height of i is less than the neighbors.
            res += min(height[i+1] - height[i], abs(height[i] - prevHeight))
            prevHeight = height[i]
            print("Result: ", res, '\n')
            # 2: 2, 0, 1
            # 2, 1
        elif height[i] < prevHeight and height[i] > height[i+1]:
            print(f"\tSTATE 3\nCurrent Amount: {res}\nCurrent Height: {height[i]} | Prev Height: {prevHeight} | Next Height: {height[i+1]}")
            print("Result: ", res)
            print(prevHeight - height[i])
            res += prevHeight - height[i]
            prevHeight = height[i]
            print("Result: ", res,
                  '\n')
        elif height[i] > prevHeight and height[i] < height[i+1]:
            print(f"\tSTATE 4\nCurrent Amount: {res}\nCurrent Height: {height[i]} | Prev Height: {prevHeight} | Next Height: {height[i+1]}")
            print("Result: ", res)
            print(height[i+1] - height[i])
            print(height[i] - prevHeight)
            res += min(height[i+1] - height[i], abs(height[i] - prevHeight))
            prevHeight = height[i]
            print("Result: ", res,
                  '\n')
    return res
print(trap([4, 2, 0, 3, 2, 5]))
