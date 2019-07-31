from collections import defaultdict
class  Solution(object):
    """docstring for  Solution"""
    def __init__(self):
        self.INT_SIZE=32

    def __str__(self):
        string = "Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer."
        return string
        
    def solution1(self, lst):
        counts = defaultdict(int)
        for i in lst:
            counts[i] += 1

        # check which number's count is not 3
        for key, val in counts.items():
            if val != 3:
                return key

        return None

    def solution2(self, lst):
        result = 0
        for i in range(self.INT_SIZE):
            x = 1 << i
            sm = 0
            for j in lst:
                if (x & j):
                    sm += 1

            if sm % 3:
                result |= x
        return result