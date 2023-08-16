class Solution:
    def mySqrt(self, x: int) -> int:
        # 找最大的ans，其中满足 ans*ans <= x
        left, right = 0, x
        while left < right:
            mid = (left + right + 1) // 2
            if mid * mid <= x:
                left = mid
            else:
                right = mid - 1
        return right
