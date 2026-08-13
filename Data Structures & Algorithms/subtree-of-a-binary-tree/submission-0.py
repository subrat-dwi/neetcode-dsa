# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def similarTree(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            if root1.val != root2.val:
                return False

            return similarTree(root1.left, root2.left) and similarTree(root1.right, root2.right)

            
        stack = [root]

        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                isSubtree = similarTree(node, subRoot)
                if isSubtree:
                    return True

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
        return False