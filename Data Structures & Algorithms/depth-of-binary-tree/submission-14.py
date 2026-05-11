# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.traverse(root,0,1)
    
    def traverse(self,node,maxCount,counter):
        print("counter", counter)
        if not node:
            return maxCount
        left = node.left
        right = node.right

        counter += 1
        if left:
            maxCount = max(self.traverse(left,maxCount,counter),maxCount)
            maxCount = max(counter,maxCount)
        if right:
            maxCount = max(self.traverse(right,maxCount,counter),maxCount)
            maxCount = max(counter,maxCount)
        counter -= 1
        maxCount = max(counter,maxCount)
        return maxCount
