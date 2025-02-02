n = 6
edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]

def magnificentSets(n, edges):
    adj = defaultdict(list)
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    def chains(source):
        Q = deque([source])
        component = set([source])

        while Q:
            node = Q.popleft()
            for neighbor in adj[node]:
                if neighbor in component:
                    continue
                Q.append(neighbor)
                component.add(neighbor)
                visit.add(neighbor)
        return component

    def longest_path(source):
        Q = deque([(source, 1)])
        distance = {source:1}

        while Q:
            node, length = Q.popleft()
            for neighbor in adj[node]:
                if neighbor in distance:
                    if distance[neighbor] == length:
                        return -1
                    continue
                Q.append((neighbor, length +1))
                distance[neighbor] = length + 1
        return max(distance.values())
        
    visited = set()
    res = 0

    for i in range(1, n+1):
        if i in visited:
            continue
        visited.add(i)

        components = chains(i)

        max_count = 0
        for source in components:
            length = longest_path(source)
            if length == -1:
                return -1
            max_count = max(max_count, length)
        res += max_count
    return res        

        
    

print(magnificentSets(n, edges))
