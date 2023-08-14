# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        successor = None  # 用来保存后继节点
        curr = root  # 从根节点开始搜索

        while curr is not None:
            if curr.val > p.val:
                successor = curr  # 如果当前节点值大于 p 的值，说明后继节点可能在左子树中，暂时保存当前节点并继续搜索左子树
                curr = curr.left
            else:
                curr = curr.right  # 否则，继续搜索右子树

        return successor
