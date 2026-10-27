# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ret = [[]]
        q = deque([(root, 0)])

        while q:
            # get the current node
            curNode, curLevel = q.pop()

            # if level not represented in the return list, add it
            if len(ret)-1 < curLevel:
                ret.append([])

            # add the val to the associated level
            ret[curLevel].append(curNode.val)

            # the order in which we add right/left helps us maintain order in the return
            if curNode.right:
                q.append((curNode.right, curLevel+1))
            if curNode.left:
                q.append((curNode.left, curLevel+1))
            

        # once we've processed the the full tree we can return
        return ret