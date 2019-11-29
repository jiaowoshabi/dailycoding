class Solution(object):

    def solution(self, n):
        NUMBITS=32
        reversed_num = 0
        for i in range(NUMBITS):
            j = n >> i & 1
            reversed_num += j << (NUMBITS-i-1)
        return reversed_num