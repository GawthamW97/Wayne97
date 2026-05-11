# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.swap(root,root.left,root.right)
        return root

    def swap(self,curr,l,r):
        if not curr:
            return
        curr.left = r
        curr.right = l
        if curr.left:
            leftNode = curr.left
            self.swap(leftNode,leftNode.left,leftNode.right)
        if curr.right:
            rightNode = curr.right
            self.swap(rightNode,rightNode.left,rightNode.right)

