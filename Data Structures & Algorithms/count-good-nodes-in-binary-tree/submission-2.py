# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,maxCount):
            if not node:
                return 0
            count = 1 if node.val >= maxCount else 0
            maxCount = max(maxCount,node.val)
            count += dfs(node.left,maxCount)
            count += dfs(node.right,maxCount)
            return count
        return dfs(root,root.val)