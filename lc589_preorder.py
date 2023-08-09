from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.seq = []

    def preorder(self, root: Node) -> List[int]:
        self.dfs(root)
        return self.seq

    def dfs(self, root: Node):
        if root is None:
            return
        self.seq.append(root.val)
        for child in root.children:
            self.dfs(child)
