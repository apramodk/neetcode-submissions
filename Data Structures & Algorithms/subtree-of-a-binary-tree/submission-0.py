# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # lets to bfs so we can easily exit
        q = deque([root])

        while q:
            curNode = q.pop()
            if not curNode:
                continue

            if curNode.val == subRoot.val:
                if self.isSameTree(curNode, subRoot):
                    return True

            q.append(curNode.left)
            q.append(curNode.right)

        return False

    def isSameTree(self, p, q) -> bool:
        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        
        if not p and not q:
            return True
        
        return False