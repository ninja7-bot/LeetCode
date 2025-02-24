preorder = [1,2,4,5,3,6,7]
postorder = [4,5,2,6,7,3,1]

def constructFromPrePost(preorder, postorder):
        if not preorder or not postorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]
        post_index = 0

        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            
            while stack and stack[-1].val == postorder[post_index]:
                stack.pop()
                post_index += 1
            
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            
            stack.append(node)
        
        return root

constructFromPrePost(preorder, postorder)
