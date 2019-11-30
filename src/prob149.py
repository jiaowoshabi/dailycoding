import heapq
from math import sqrt

class Solution:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def solution(self, lst, pt, k):
        hp = []

        for x,y in lst:
            eudistance = sqrt(abs(pt[0]-x)**2 + abs(pt[1]-y)**2)
            heapq.heappush(hp, (eudistance, (x,y)))

        res = []
        for i in range(k):
            _, e = heapq.heappop(hp)
            res.append(e)

        return res