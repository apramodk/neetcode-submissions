# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
       # kth smallest node, if we index from 1. 1 <= k <= |nodes in tree|
       # we basically wanna traverse the tree to find the smallest value, the left most child,

        l = list()
       # first we wanna get to the smallest int in the bst, by going down continuously
        def dfs(root: Optional[TreeNode]):
            nonlocal l
            if not root:
                return 
            
            dfs(root.left)
            l.append(root.val)
            dfs(root.right)

        dfs(root)
        return l[k-1]