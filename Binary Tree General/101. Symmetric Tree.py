class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_symmetric(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return (
                is_symmetric(left.left, right.right) and
                is_symmetric(left.right, right.left)
            )
        
        return is_symmetric(root.left, root.right)