class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum
        
        remainingSum = targetSum - root.val
        return self.hasPathSum(root.left, remainingSum) or self.hasPathSum(root.right, remainingSum)
