from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._preorder_helper(root, result)
        return result
    
    def _preorder_helper(self, node: Optional[TreeNode], result: List[int]) -> None:
        if node is None:
            return
        result.append(node.val)
        self._preorder_helper(node.left, result)
        self._preorder_helper(node.right, result)
