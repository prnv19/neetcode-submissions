# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # dfs
        # def valid(node, left, right):
        #     if not node:
        #         return True
        #     if left < node.val < right:
        #         return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        #     return False
        # return valid(root, -float('inf'), float('inf'))

        # bfs
        q = deque([(root, -float('inf'), float('inf'))])

        while q:
            node, left, right = q.popleft()

            if not left < node.val < right:
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))

        return True
        