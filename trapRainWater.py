from heapq import heappush, heappop
def trapRainWater(heightMap):
    ROWS = len(heightMap)
    COLS = len(heightMap[0])

    minHeap = []

    for r in range(ROWS):
        for c in range(COLS):
            if r in [0, ROWS-1] or c in [0, COLS-1]:
                heappush(minHeap, (heightMap[r][c], r, c))
                heightMap[r][c] = -1
    
    res = 0
    max_h = -1
    while minHeap:
        h, r, c = heappop(minHeap)
        max_h = max(max_h, h)
        res += max_h - h

        neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
        for NR, NC in neighbors:
            if (NR < 0 or NC < 0 or
                NR == ROWS or NC == COLS or
                heightMap[NR][NC] == -1):
                    continue
            heappush(minHeap, (heightMap[NR][NC], NR, NC))
            heightMap[NR][NC] = -1
    return res
                
    
print(trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
