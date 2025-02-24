def mostProfitablePath(edges, bob, amount):
        n = len(amount)
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        bobTime = {}
        
        parent = {0: -1}
        def dfs_build_path(node, par):
            parent[node] = par
            for neighbor in graph[node]:
                if neighbor == par:
                    continue
                dfs_build_path(neighbor, node)
        
        dfs_build_path(0, -1)
        
        time = 0
        cur = bob
        while cur != -1:
            bobTime[cur] = time
            time += 1
            cur = parent[cur]
        
        maxIncome = float("-inf")
        
        def dfs_alice(node, par, time, currentIncome):
            nonlocal maxIncome
            if node in bobTime:
                if time < bobTime[node]:
                    currentIncome += amount[node]
                elif time == bobTime[node]:
                    currentIncome += amount[node] // 2
                else:
                    currentIncome += 0
            else:
                currentIncome += amount[node]
            
            isLeaf = True
            for neighbor in graph[node]:
                if neighbor == par:
                    continue
                isLeaf = False
                dfs_alice(neighbor, node, time + 1, currentIncome)
            
            if isLeaf:
                maxIncome = max(maxIncome, currentIncome)
        
        dfs_alice(0, -1, 0, 0)
        return maxIncome
