from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)  # 初始化 left 和 right
        while left < right:
            mid = left + (right - left) // 2  # 使用这种方式避免溢出问题
            if self.validate(nums, k, mid):
                right = mid
            else:
                left = mid + 1
        return right

    # 判定函数
    def validate(self, nums: List[int], k: int, size: int) -> bool:
        box, count = 0, 1
        for num in nums:
            if box + num <= size:
                box += num
            else:
                count += 1
                box = num
        return count <= k
