# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # right side view assumes that the right most value at a given depth is what we return
        #  meaning if at a given depth level the first existing value when we look from the right 
        # is the values that represent each depth

        # My initial thought is that we could traverse through the tree in a greedy style bfs format. 
        # where we prefer always going right first, if the right value returns none, then we can assume that the left side IS
        # the right most value.
        # looking at example 2, it is important for us to ensure that we process both left and right.
        # what we could do is create a list of lists, with the value at each list being added in right first order

        # lets start by processing the tree first:
        if not root:
            return []
        ret = [[]]
        def levelOrderTraversal(root: TreeNode):
            nonlocal ret
            q = deque([(root, 0)])

            while q:
                curNode, curLevel = q.pop()

                if len(ret) < curLevel+1:
                    ret.append([])
                
                ret[curLevel].append(curNode.val)

                if curNode.left:
                    q.append((curNode.left, curLevel+1))
                if curNode.right:
                    q.append((curNode.right, curLevel+1))

        levelOrderTraversal(root)

        retfr = []
        for arr in ret:
            retfr.append(arr[0])
        
        return retfr

