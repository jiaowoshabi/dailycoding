class Solution(object):
    """docstring for Solution"""
    def __init__(self):
        pass

    def __str__(self):
        string = "Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well"
        return string

    def solution(self, lst):
        s = set(lst)
        counter = 1
        while counter in s:
            counter += 1

        return counter

    def better_solution(self, lst):
        if not lst:
            return 1
        for i, num in enumerate(lst):
            while i + 1 != lst[i] and 0 < lst[i] <= len(lst):
                v = lst[i]
                lst[i], lst[v - 1] = lst[v - 1], lst[i]
                if lst[i] == lst[v - 1]:
                    break
        for i, num in enumerate(lst, 1):
            if num != i:
                return i
        return len(lst) + 1