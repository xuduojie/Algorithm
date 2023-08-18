from typing import List


class Solution:
    alphabet = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.ans = []
        self.dfs(0, digits, "")
        return self.ans

    def dfs(self, index: int, digits: str, current_str: str) -> None:
        # 边界处理
        if index == len(digits):
            self.ans.append(current_str)
            return
        for ch in self.alphabet[digits[index]]:
            self.dfs(index + 1, digits, current_str + ch)
