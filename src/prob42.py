class Solution(object):
    def __init__(self):
        pass

    def __str__(self):
        string = ""
        return string

    def solution(self, lst, target):
        """
        define OPT be the subset of lst adds up to target
        base case:
            lst is empty and target is 0
        recursive case:
            lst[0] in subset:
                OPT(lst[1:], target-lst[0])
            lst[0] not in subset:
                OPT(lst[1:], target)
        """
        if not lst:
            return None

        res  = self.helper(lst, target)
        return res

    def helper(self, lst, target):

        if target ==0:
            return []
        elif not lst and target != 0:
            return None

        lst_copy = list(lst)

        with_last = self.helper(lst[:-1], target-lst[-1])
        without_last = self.helper(lst[:-1], target)

        if with_last is not None:
            return [lst_copy[-1]] + with_last
        elif without_last is not None:
            return without_last


    def interative_sol(self, lst, target):
        cache = [[None for _ in range(target+1)] for _ in range(len(lst)+1)]
        for i in range(len(lst)+1):
            cache[i][0] = []

        for i in range(1, len(lst)+1):
            for j in range(1, target+1):
                last = lst[i-1]
                if last > j:
                    cache[i][j] = cache[i-1][j]
                else:
                    if cache[i-1][j] is not None:
                        cache[i][j] = cache[i-1][j]
                    elif cache[i-1][j-last] is not None:
                        cache[i][j] = cache[i-1][j-last]+[last]
                    else:
                        cache[i][j] = None

        return cache[-1][-1]

    def subset_sum(self, nums, k):
        A = [[None for _ in range(k + 1)] for _ in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            A[i][0] = []

        for i in range(1, len(nums) + 1):
            for j in range(1, k + 1):
                last = nums[i - 1]
                if last > j:
                    A[i][j] = A[i - 1][j]
                else:
                    if A[i - 1][j] is not None:
                        A[i][j] = A[i - 1][j]
                    elif A[i - 1][j - last] is not None:
                        A[i][j] = A[i - 1][j - last] + [last]
                    else:
                        A[i][j] = None

        return A[-1][-1]
