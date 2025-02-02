def LSA(nums, limit):
    groups = []
    num_to_group = {}

    for num in sorted(nums):
        if not groups or abs(num - groups[-1][-1]) > limit:
            groups.append(deque())
        groups[-1].append(num)
        num_to_group[n] = len(groups) - 1

    res = []
    for n in nums:
        j = num_to_group[n]
        res.append(groups[j].poplefft())
    return res

        
