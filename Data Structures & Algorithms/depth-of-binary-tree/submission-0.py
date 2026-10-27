# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxVal = 0
        depth = 0

        def dfs(root, depth):
            nonlocal maxVal
            if not root:
                return

            depth += 1
            dfs(root.left, depth)
            dfs(root.right, depth)


            maxVal = max(maxVal, depth)

        dfs(root, depth)

        return maxVal
