graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
def eSN(graph):
    terminalNodes = []
    safe = {}
    safeNodes = []

    def DFS(node):
        if node in safe:
            return safe[node]
        safe[node] = False
        for nei in graph[node]:
            if not DFS(nei):
                return False
        safe[node] = True
        return safe[node]

    for i in range(len(graph)):
        if DFS(i):
            safeNodes.append(i)

    return safeNodes
"""                
1. Go to the index 0.
2. Check for all the nodes we can go to from 0: 1, 2.
3. Follow the 1st value of 0th Node.
4. Do Step 2.
5. 
"""
    

eSN(graph)
