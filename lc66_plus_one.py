class Solution:
    def plusOne(self, digits: list) -> list:
        digits[-1] += 1  # 首先把最后一位加一            [1,2,10]
        for i in range(len(digits) - 2, -1, -1):  # 从低位到高位遍历
            if digits[i + 1] >= 10:  # 如果低位>=10，那前一位的高位可以加一
                digits[i + 1] = digits[i + 1] % 10
                digits[i] += 1
            else:  # 如果我们的在某一位的数字没有产生进位的话，那么之后的高位再也不可能进位了，直接跳出
                break

        if digits[0] >= 10:  # 对最高位稍做处理，如解题思路中的[9,9,9]
            digits = [1] + digits
            digits[1] %= digits[1]

        return digits
