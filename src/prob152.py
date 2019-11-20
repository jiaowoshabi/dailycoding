from random import random
from bisect import bisect_left

class Solution:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def solution(self, nums, probs):
        r = random()

        s = 0

        for num, prob in zip(nums, probs):
            s += prob
            if s >= r:
                return num

    def better_solution(self, nums, probs):
        def preprocess(probs):
            sort_probs = list()

            curr_val = 0
            for i in probs:
                curr_val += i
                sort_probs.append(curr_val)

            return sort_probs

        r = random()
        sort_probs = preprocess(nums)
        idx = bisect_left(sort_probs, r)
        return nums[idx]