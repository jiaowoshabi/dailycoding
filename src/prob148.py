class Solution:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def solution(self, n):
        if n == 0:
            return []
        if n == 1:
            return [0, 1]

        prev_gray_code = self.solution(n-1)

        result = []
        for code in reversed(prev_gray_code):
            result.append((1 << (n-1)) + code)
        return  prev_gray_code + result