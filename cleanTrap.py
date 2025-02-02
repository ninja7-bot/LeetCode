def cleanTrap(height):
    LENGTH = len(height) - 1
    res = 0
    prevHeight = 0

    for i in range(0, LENGTH + 1):
        if i == 0 or i == LENGTH:
            continue

        if height[i] > height[i + 1] and height[i] > prevHeight:
            prevHeight = height[i]
            continue

        elif height[i] < prevHeight and height[i] < height[i + 1]:
            res += min(height[i + 1] - height[i], abs(height[i] - prevHeight))
            prevHeight = height[i]

        elif height[i] < prevHeight and height[i] > height[i + 1]:
            res += prevHeight - height[i]
            prevHeight = height[i]

        elif height[i] > prevHeight and height[i] < height[i + 1]:
            res += min(height[i + 1] - height[i], abs(height[i] - prevHeight))
            prevHeight = height[i]

    return res
