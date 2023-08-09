# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.seq = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        return self.seq

    def dfs(self, root: TreeNode):
        if root is None:
            return
        self.dfs(root.left)
        self.seq.append(root.val)
        self.dfs(root.right)
