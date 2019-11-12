class Solution:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def solution(self, lst, index):
        if len(lst) <= 1:
            return None
        lengh = len(lst)
        for dis in range(1,len(lst)):
            if index+dis < lengh and lst[index+dis] > lst[index]:
                return index+dis
            elif index-dis >= 0 and lst[index-dis] > lst[index]:
                return index-dis

    def better_solution(self, lst, j):
        """
        preprocess the array and use lookup table
        """
        if j >= len(lst):
            return None
            
        cache = [None for _ in range(len(lst))]

        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                cache[i+1] = i
            elif lst[i+1] > lst[i]:
                cache[i] = i+1

        for i, val in enumerate(cache):
            if val is None:
                cache[i] = self.solution(lst, i)

        return cache[j]