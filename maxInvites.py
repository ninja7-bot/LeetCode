def maxInv(favorite):
    n = len(favorite)
    visited = [False] * n
    longest_chain = 0
    length_2 = []

    
    for i in range(n):
        if visited[i]:
            continue
        start, curr = i, i
        curr_set = set()

        while not visited[curr]:
            visited[curr] = True
            curr_set.add(curr)
            curr = favorite[curr]

        if curr in curr_set:
            l = len(curr_set)
            while start != curr:
                l -= 1
                start = favorite[start]
            longest_chain = max(longest_chain, l)

            if l == 2:
                length_2.append([curr, favorite[curr]])

    invert = defaultdict(list)
    
    for dst, src in enumerate(favorite):
        invert[src].append(dst)

    def BFS(source_node, parent_node):
        Q = deque([(source_node, 0)])
        max_length = 0

        while Q:
            node, length = Q.popleft()
            
            if node == parent:
                continue
            max_length = max(max_length, length)

            for neighbor in invert[node]:
                Q.append((neighbor, length+1))
        return max_length

    chainSum = 0

    for i1, i2 in length_2:
        chainSum += BFS(i1, i2) + BFS(i2, i1) + 2

    return max(chainSum, longest_chain)
