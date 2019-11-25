from math import inf
class Solution:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def solution(self, num, i=1):
        if num == 0:
            return 0

        min_sqrt_num  = inf
        while num - i*i >= 0:
            min_sqrt_num = min(min_sqrt_num, self.solution(num - i*i)+1)
            i += 1

        return min_sqrt_num


