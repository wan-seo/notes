# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        def inorder(stack):
            res = []                
            while stack:
                node = stack.pop()
                if node:
                    stack.append(node.right)
                    stack.append(node)
                    stack.append(node.left)
                else:
                    if stack:
                        node = stack.pop()
                        res.append(node.val)
            return res
        def inorder(stack):
            traversal = []
            if stack:
                node = stack.pop()
                if node:
                    inorder(node.left)
                    inorder(node)
                    inorder(node.right)
                else:
                    node = stack.pop()
                    traversal.append(node.val)
        res = inorder(stack)
        return res


        

        
        