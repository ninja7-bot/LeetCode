"""
tree = [    [],
                [],        [],
            [],     [],[],     [],
                ]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.recovered = set()
        
        if root == -1:
            root.val = 0
            self.recoverTree(root)

    def recoverTree(treeNode):
        if not node:
            return
        self.recovered.add(treeNode)
            
        if treeNode.left != null:
            treeNode.left.val == val * 2 + 1
            self.recovered.add(treeNode.left)
        if treeNode.right != null:
            treeNode.right.val == val * 2 + 2
            self.recovered.add(treeNode.right)
    def find(target) -> bool:
        if target in tree:
            return True
        return False
