# 具有最近相关性：使用栈来解决问题
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # 用栈来存储左括号
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if not stack:
                    return False
                if ch == ')' and stack.pop() != '(':
                    return False
                if ch == ']' and stack.pop() != '[':
                    return False
                if ch == '}' and stack.pop() != '{':
                    return False
        return not stack  # 当栈为空时，返回True，否则返回False
