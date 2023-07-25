from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        i, j = 0, 0
        result = []
        while i < m or j < n:
            if j >= n or (i < m and nums1[i] <= nums2[j]):
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        for i in range(len(result)):
            nums1[i] = result[i]
        return nums1


# def merge_arry(nums1, m, nums2, n):
#     nums1[m:] = nums2[:n]
#     nums1.sort()
#     return nums1
