from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[n] = nums[i]
            n += 1
    while n < len(nums):
        nums[n] = 0
        n += 1

