# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.seen = []
        
        def dfs(node):
            if not node:
                return
            self.seen.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root.left)
        self.seen.append(root.val)
        dfs(root.right)
        
        return sorted(self.seen)[k-1]