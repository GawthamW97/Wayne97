# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.seen = defaultdict(list)

        level = 0

        self.depth(root,0)

        return [v for k,v in self.seen.items()]

    def depth(self,node, level):
        if not node:
            return
        level += 1
        self.seen[level].append(node.val)
        self.depth(node.left,level)
        self.depth(node.right,level)
        return



