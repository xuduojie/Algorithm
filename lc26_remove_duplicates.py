from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                nums[n] = nums[i]
                n += 1
        return n


"""
    保序操作数组的过滤器题目模板代码
        n = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:  # 每个过滤器条件不同
                nums[n] = nums[i]
                n += 1
"""
