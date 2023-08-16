from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
        if ans != [] and len(ans) != 1:
            n = len(ans) - 1
            return [ans[0], ans[n]]
        elif len(ans) == 1:
            return [ans[0], ans[0]]
        else:
            return [-1, -1]
