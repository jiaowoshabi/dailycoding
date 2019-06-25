class Solution:
    def __init__(self):
        pass

    def __str__(self):
        string = "Given a list of numbers and a number k, return whether any two numbers from the list add up to k."
        return string

    def two_sum(self, lst, k):
        if len(lst) <= 1:
            return False
        
        length = len(lst)
        for idx, val in enumerate(lst):
            fast = idx + 1
            while (fast < length) and (lst[idx] + lst[fast] != k):
                fast += 1

            if (fast < length) and (lst[idx] + lst[fast]) == k:
                return True

        return False

    def better_two_sum(self, lst, k):
        seen = set()
        for i in lst:
            if k - i in seen:
                return True
            seen.add(i)
            
        return False