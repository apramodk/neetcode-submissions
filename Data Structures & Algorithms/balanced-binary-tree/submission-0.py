# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        return self.countHeight(root) != -1
    
    def countHeight(self, root) -> int:
        if root is None:
            return 0
        
        heightR = self.countHeight(root.right)
        heightL = self.countHeight(root.left)

        if (abs(heightL - heightR) > 1) or (heightL == -1 or heightR == -1) :
            return -1

        return max(heightR+1, heightL+1)