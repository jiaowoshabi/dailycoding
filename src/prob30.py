class Solution:
    def __init__(self):
        pass

    def my_solution(self, lst):
        """
        slow&fast pointers
        """
        if len(lst) < 2:
            return 0

        tot = 0
        left_max_arr = [0 for _ in lst]
        right_max_arr = [0 for _ in lst]

        left_max = 0
        for idx, val in enumerate(lst):
            left_max = max(val, left_max)
            left_max_arr[idx] = left_max

        right_max = 0
        for idx in range(len(lst)-1, -1, -1):
            right_max = max(lst[idx], right_max)
            right_max_arr[idx] = right_max

        for idx, val in enumerate(lst):
            tot += min(left_max_arr[idx], right_max_arr[idx]) - val

        return tot

    def better_solution(self, arr):
        """
        slow&fast pointers
        """
        if len(arr) < 2:
            return 0

        total = 0
        max_i = arr.index(max(arr))

        left_max = arr[0]
        for num in arr[1:max_i]:
            print("left", left_max - num)
            print("tot", total)
            total += left_max - num
            left_max = max(left_max, num)

        right_max = arr[-1]
        for num in arr[-2:max_i:-1]:
            print("right", right_max - num)
            total += right_max - num
            right_max = max(right_max, num)

        return total
