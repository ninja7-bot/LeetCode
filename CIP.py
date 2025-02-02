numCourses = 5
prerequisites = [[4,3],[4,1],[4,0],[3,2],[3,1],[3,0],[2,1],[2,0],[1,0]]
queries = [[1,4],[4,2],[0,1],[4,0],[0,2],[1,3],[0,1]]

def cIP(numCourses, prerequisites, queries):
    # 3, [1, 0], [0, 1] -> The num of courses are 3 and the prerequisite is that to take course 0 you need to have course 1.
    # The query is, what if we take course 1, do we need to have course 0?

    # {0: 1, 1: 'False'}
    # [0, 1] -> Dict Check 0 requires any course. If some value is found then return True.
    # Dict Check: If 0 -> 1, True ? False

        reachable = [[False] * numCourses for _ in range(numCourses)]
        for u, v in prerequisites:
            reachable[u][v] = True

        # Step 2: Compute transitive closure using Floyd-Warshall
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])

        # Step 3: Answer queries
        return [reachable[u][v] for u, v in queries]

    

cIP(numCourses, prerequisites, queries)
