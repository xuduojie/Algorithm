# 中缀表达式可以先转换为后缀表达式（逆波兰式）
class Solution:
    def calculate(self, s: str) -> int:
        # 创建栈来保存需要进行 +， - 运算符的所有数字（把- 运算符改成负数放到栈中）。
        stack = []
        pre_op = '+'
        num = 0
        for i, each in enumerate(s):
            if each.isdigit():
                num = 10 * num + int(each)
            if i == len(s) - 1 or each in '+-*/':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                elif pre_op == '/':
                    top = stack.pop()
                    if top < 0:
                        stack.append(int(top / num))
                    else:
                        stack.append(top // num)
                pre_op = each
                num = 0
        return sum(stack)
