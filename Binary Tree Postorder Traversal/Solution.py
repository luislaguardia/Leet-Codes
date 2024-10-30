from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._postorder_helper(root, result)
        return result
    
    def _postorder_helper(self, node: Optional[TreeNode], result: List[int]) -> None:
        if node is None:
            return
        self._postorder_helper(node.left, result)
        self._postorder_helper(node.right, result)
        result.append(node.val)
