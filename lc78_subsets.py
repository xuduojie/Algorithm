from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.recur(nums, 0, [])
        return self.ans

    def recur(self, nums, i, chosen):
        n = len(nums)
        # 递归边界
        if i == n:
            self.ans.append(chosen[:])  # 注意，将chosen的副本添加到结果中，而不是直接添加chosen本身
            return None
        # 每层的相似逻辑：nums[i]选或不选
        self.recur(nums, i + 1, chosen)
        chosen.append(nums[i])
        self.recur(nums, i + 1, chosen)
        # 还原现场
        chosen.pop()
