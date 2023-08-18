from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2 += sorted(set(arr1)-set(arr2))
        arr1.sort(key=arr2.index)
        return arr1
