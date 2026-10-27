# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # a good node is defined as any leaf node, where the path from it to the root is a greater value
        # we are given a non optional root, meaning we will have atleast the root node.
        # if x = node.val, -100 <= x <= 100
        # can I modify the tree in any way?
        # do i have any space constraint?

        # to solve this we basically want to keep track of a global counter, and a local minimum.

        # so to decompose this problem:

        # we have to traverse the to the leaf nodes of a given root
        # keep track of a local maximum, and ensure that the value of whatever node we're on is greater than our local maximum.
        counter = 0

        def dfs(root: TreeNode, node: Optional[TreeNode]):
            nonlocal counter

            if not node:
                return

            # what if the vals are equal? I assume we always count the root as 1, 
            # because root to root contains no value less than itself in the path.
            if root.val <= node.val:
                counter += 1
                root = node

            dfs(root, node.left)
            dfs(root, node.right)

        dfs(root, root)

        return counter