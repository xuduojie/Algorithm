# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 使用father这个哈希表，缓存父节点的信息
        father = {}
        self.calcFather(root, None, father)
        redNodes = set()
        # 将所有p节点的父节点全部获取，加入redNodes中
        while p:
            redNodes.add(p)
            p = father[p]

        # q节点第一个父节点碰撞到的，直接返回
        while q not in redNodes:
            q = father[q]
        return q

    # 递归模板函数
    def calcFather(self, root: TreeNode, parent: 'TreeNode', father: dict):
        # 递归终止条件
        if root is None:
            return
        father[root] = parent
        self.calcFather(root.left, root, father)
        self.calcFather(root.right, root, father)


