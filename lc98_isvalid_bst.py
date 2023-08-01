# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 边界处理
        return self.check(root, float('-inf'), float('inf'))

    def check(self, root: Optional[TreeNode], rangeLeft: float, rangeRight: float) -> bool:
        if root is None:
            return True
        if root.val <= rangeLeft or root.val >= rangeRight:
            return False
        return self.check(root.left, rangeLeft, root.val) and self.check(root.right, root.val, rangeRight)
