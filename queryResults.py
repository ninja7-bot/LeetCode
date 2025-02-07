def queryResults(limit, queries):
    balls = limit + 1
    D = {i: 0 for i in range(balls)}  # Initialize ball colors
    result = []
    distinct_colors = set()

    for ball, color in queries:
        if D[ball] != color:  # Process only if the color changes
            if D[ball] > 0:
                distinct_colors.discard(D[ball])  # Remove the old color if it exists
            if color > 0:
                distinct_colors.add(color)  # Add the new color if valid

            D[ball] = color

        result.append(len(distinct_colors))

    return result
limit = 4
queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
print(queryResults(limit, queries))  # Expected Output: [1, 2, 2, 3, 4]
