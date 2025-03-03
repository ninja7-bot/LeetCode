def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index_map = {num: i for i, num in enumerate(arr)}
        n = len(arr)
        dp = defaultdict(lambda: 2) 
        max_len = 0

        for j in range(n):
            for i in range(j):
                diff = arr[j] - arr[i]
                if diff in index_map and index_map[diff] < i:
                    k = index_map[diff]
                    dp[i, j] = dp[k, i] + 1 
                    max_len = max(max_len, dp[i, j])

        return max_len if max_len >= 3 else 0   
