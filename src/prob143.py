class Solution:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def solution(self, lst, pivot):
        first = []
        second = []
        third = []
        for i in lst:
            if i < pivot:
                first.append(i)
            elif i == pivot:
                second.append(i)
            else:
                third.append(i)

        return first+second+third

    def better_solution(self, lst, pivot):
        i = 0
        j = 0
        k = len(lst) - 1
        while j < k:
            if lst[j] == pivot:
                j += 1
            elif lst[j] < pivot:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j += 1
            else:
                lst[j], lst[k] = lst[k], lst[j]
                k -= 1
        return lst
