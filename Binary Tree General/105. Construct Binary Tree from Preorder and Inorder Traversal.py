# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        i = inorder.index(root_val) # inorder_root_index

        root.left = self.buildTree(preorder[1:(i + 1)], inorder[:i])
        root.right = self.buildTree(preorder[(i + 1):], inorder[(i+1):])

        return root