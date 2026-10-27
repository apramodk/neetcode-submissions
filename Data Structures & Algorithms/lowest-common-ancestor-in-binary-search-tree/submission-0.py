# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # in a bst, we have some root node, which contains a pivot value, 
        # any value that is less than the pivot, will go to the left.
        # any value that is greater than the pivot will go to the right.

        # we are guaranteed the p and q will exist within the tree
        sNode = p if p.val < q.val else q
        bNode = p if p.val > q.val else q

        # as we go through the tree, we want to see if there is any case such that we cannot find a node ,ancestor,
        # such that sNode <= ancestor <= bNode

        ancestor = root
        sval = sNode.val
        bval = bNode.val

        while ancestor:
            # exit condition is if the ancestor is <= bval, and >= sval 
            if ancestor.val <= bval and ancestor.val >= sval:
                return ancestor

            # if the biggest value is less than the ancestor, move left, if the smaller value is larger than the pivot move right
            if ancestor.val > bval:
                print(f"moved left: {ancestor.val} > {bval}")
                ancestor = ancestor.left
            elif ancestor.val <  sval:
                print(f"moved right: {ancestor.val} < {sval}")
                ancestor = ancestor.right

        return root