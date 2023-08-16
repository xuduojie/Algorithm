from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[right]:  # 条件满足（true，即1）
                right = mid
            else:
                left = mid + 1
        return nums[right]
