# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        m = preorder[0]
        root = TreeNode(m)
        mIndex = inorder.index(m)
        root.left = self.buildTree(preorder[1:mIndex+1],inorder[:mIndex])
        root.right = self.buildTree(preorder[mIndex + 1:],inorder[mIndex+1:])
        return root
        