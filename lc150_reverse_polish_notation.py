from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                # 如果是运算符，则从栈中弹出两个数字进行计算
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(float(a)/float(b)))
            else:
                # 如果是数字，则将其压入栈中
                stack.append(int(token))
        return stack[0]