edges =[[2,5],[1,3],[3,5],[1,4],[2,3]]

def findRedundantConnection(edges):
    visited = []
    canRemove = []

    for edge in edges:
        print(f"{edge[0]} -> {edge[1]}")
        if edge[0] in visited and edge[1] in visited:
            canRemove.append(edge)
        elif edge[0] in visited and not edge[1] in visited:
            visited.append(edge[1])
        elif edge[0] not in visited and edge[1] in visited:
            visited.append(edge[0])
        else:
            visited.append(edge[0])
            visited.append(edge[1])
    print(f"Visited: {visited}")
    print(f"Can Remove: {canRemove}")
    _visited = {}
    for edge in canRemove:
        print(f"{edge[0]} -> {edge[1]}")
        if edge[1] in _visited.keys():
            _visited[edge[1]] += 1
        else:
            _visited[edge[0]] = 0
            _visited[edge[1]] = 1
    print(f"Visited: {_visited}")
    max_value = max(_visited.values())
    max_visited = max(k for k in _visited if _visited[k] == max_value)
    res = canRemove[-1]
    print(max_visited)
    for edge in canRemove[::-1]:
        if edge[1] == max_visited:
            return edge
    return res

print(findRedundantConnection(edges))
"""
def findRedundantConnection(edges):
    visited = {}
    canRemove = []
    for edge in edges:
        print(f"{edge[0]} -> {edge[1]}")
        if edge[1] in visited.keys():
            visited[edge[1]] += 1
            if visited[edge[1]] > 1 and edge not in canRemove:
                canRemove.append(edge)
        else:
            visited[edge[0]] = 0
            visited[edge[1]] = 1
    
    max_visited = max(visited, key= visited.get)
    print(max_visited)
    for edge in canRemove[::-1]:
        if edge[1] == max_visited:
            return edge
    print(visited)
    print(canRemove)
    return canRemove[-1]
print(findRedundantConnection(edges))
"""
