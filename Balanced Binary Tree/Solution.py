class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkHeight(root) != -1
    
    def checkHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        leftHeight = self.checkHeight(node.left)
        if leftHeight == -1:
            return -1
        
        rightHeight = self.checkHeight(node.right)
        if rightHeight == -1:
            return -1
        
        if abs(leftHeight - rightHeight) > 1:
            return -1
        
        return 1 + max(leftHeight, rightHeight)
