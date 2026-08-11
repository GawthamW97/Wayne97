"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(newNode):

            if newNode in oldToNew:
                return oldToNew[newNode]
            
            curr = Node(newNode.val)
            oldToNew[newNode] = curr
            for nei in newNode.neighbors:
                curr.neighbors.append(dfs(nei))

            return curr
        
        return dfs(node) if node else None
