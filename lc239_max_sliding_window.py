from collections import deque


def max_sliding_window(nums, k):
    if not nums:
        return []

    result = []
    window = deque()

    for i, num in enumerate(nums):
        # 单调队列：保证窗口中的元素是递减的，如果当前元素比队列中最后一个元素大，则将队列中的最后一个元素移除
        while window and nums[window[-1]] < num:
            window.pop()

        # 将当前元素的索引加入队列
        window.append(i)

        # 检查窗口的左侧是否超出范围，如果超出，则移除左侧元素
        if window[0] == i - k:
            window.popleft()

        # 当窗口大小达到k时，记录窗口中的最大值
        if i >= k - 1:
            result.append(nums[window[0]])

    return result
