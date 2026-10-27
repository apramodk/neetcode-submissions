# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case, do nothing if no root exist
        if not root:
            return root

        self.invertTree(root.left)
        self.invertTree(root.right)

        # swap left & right
        root.left, root.right = root.right, root.left

        return root