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

        def dfs(n):

            if n in oldToNew:
                return oldToNew[n]

            curr = Node(n.val)
            oldToNew[n] = curr

            for nei in n.neighbors:
                curr.neighbors.append(dfs(nei))

            return curr

        return dfs(node) if node else None