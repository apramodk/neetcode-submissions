# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        q = deque([(root, (-2**32, 2**32))])

        while q:
            curNode, bounds = q.pop()
            lower = bounds[0]
            upper = bounds[1]

            # if we are out of bounds immediately return False
            if curNode.val <= lower or curNode.val >= upper:
                return False

            # if we can go left, lowerBound = current lowerBound, upperBound = the current value
            if curNode.left:
                tmp = (curNode.left, (lower, curNode.val))
                q.append(tmp)
            # if we can go right,lowerBound = current value, upperBound = current upperBound
            if curNode.right:
                tmp = (curNode.right, (curNode.val, upper))
                q.append(tmp)

        return True