# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def depth(node):
            if not node:
                return [0,True]
            leftSide = depth(node.left)
            rightSide = depth(node.right)
            status = leftSide[1] and rightSide[1] and abs(leftSide[0] - rightSide[0]) <= 1

            return [1 + max(leftSide[0],rightSide[0]),status]

        return depth(root)[1]

        
