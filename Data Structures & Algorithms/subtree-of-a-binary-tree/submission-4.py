# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same(node1, node2):
            if not node1 and not node2:
                return True
            elif node1 and node2 and node1.val == node2.val:
                left = is_same(node1.left, node2.left)
                right = is_same(node1.right, node2.right)
                return left and right
            else:
                return False
        
        def dfs(root, subroot):
            if not root:
                return False
            
            if is_same(root, subRoot):
                return True
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        return dfs(root, subRoot)
            

        