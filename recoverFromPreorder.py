class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def recoverTreeToList(traversal):
    stack = []
    i = 0
    n = len(traversal)
    while i < n:
        level = 0
        while i < n and traversal[i] == '-':
            level += 1
            i += 1
        num = 0
        while i < n and traversal[i].isdigit():
            num = num * 10 + int(traversal[i])
            i += 1
        node = TreeNode(num)
        while len(stack) > level:
            stack.pop()
        if stack:
            parent = stack[-1]
            if parent.left is None:
                parent.left = node
            else:
                parent.right = node
        stack.append(node)
    return stack[0] if stack else None

traversal = "1-2--3--4-5--6--7"
print(recoverTreeToList(traversal))  # Expected Output: [1, 2, 5, 3, 4, 6, 7]
