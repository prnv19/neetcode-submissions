# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root , depth):
            if not root:
                return depth
            
            return max(dfs(root.left, 1 + depth), dfs(root.right, 1 + depth))
        return dfs(root, 0)
            



        