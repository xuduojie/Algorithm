from typing import List


class Solution:
    def moveZero(self, nums: List[int]) -> None:
        n = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[n] = nums[i]
                n += 1
        # 补零
        while n < len(nums):
            nums[n] = 0
            n += 1
