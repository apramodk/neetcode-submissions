"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.copiedNodes = dict()

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # if no node exists
        if not node:
            return None

        val = node.val
        if val in self.copiedNodes:
            return self.copiedNodes[val]
        
        cNode = Node(val) 
        self.copiedNodes[val] = cNode

        for neighbor in node.neighbors:
           cNode.neighbors.append(self.cloneGraph(neighbor))

        return cNode