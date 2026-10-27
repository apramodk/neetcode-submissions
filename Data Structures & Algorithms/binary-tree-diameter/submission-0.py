# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: 
        # what is the diameter actually?
        # - it feels like it is just the depth of the longest sub-tree
        # - based on ex 1, and 2, this seems to be correct
        # we could just dfs traverse, keep track of the depth and return the max depth we find
        md = 0

        def dfs(root) -> int:
            nonlocal md
            # once we're at a leaf node we can check the depth
            if not root:
                return 0
            

            # otherwise, we go left and right, and increment depth by 1
            right = dfs(root.right)
            left = dfs(root.left)

            height = max(left,right) + 1
            md = max(md, right+left)

            return height
            
        dfs(root)

        return md