class Solution(object):
    """docstring for Solution"""
    def __init__(self):
        pass

    def __str__(self):
        string = "Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i."
        return string

    def solution(self, lst):
        prod = 1
        for i in lst:
            prod *= i

        return [prod/i for i in lst]

    def no_div(self, lst):
        def multiply(lst):
            prod = 1
            for i in lst:
                prod *= i
            return prod

        al = set(lst)
        return [multiply(list(al-set([i]))) for i in lst]

    def better_solution(self, lst):
        if len(lst) == 0:
            return lst
        elif len(lst) == 1:
            return [1]
        # generate prefix lst
        prefix = []
        for i in lst:
            if prefix:
                prefix.append(prefix[-1] * i)
            else:
                prefix.append(i)

        # generate suffix lst
        suffix = []
        for i in list(reversed(lst)):
            if suffix:
                suffix.append(suffix[-1] * i)
            else:
                suffix.append(i)

        suffix = list(reversed(suffix))
        print(prefix)
        print(suffix)

        result = []
        for i in range(len(lst)):
            if i == 0:
                result.append(suffix[i+1])
            elif i == len(lst) - 1:
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1] * suffix[i+1])
        return result
        