class MinStack:
    def __init__(self):
        self.s = []  # 用来存储数据元素的栈本身
        self.preMin = []  # 用来存储前缀最小值的栈

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.preMin:
            self.preMin.append(val)
        else:
            self.preMin.append(min(self.preMin[-1], val))

    def pop(self) -> None:
        self.s.pop()
        self.preMin.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.preMin[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
