# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ret = False
        # a tree is the same if it has the exact same values
        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

        if not p and not q:
            return True

        return False