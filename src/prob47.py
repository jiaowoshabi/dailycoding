class Solution:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def solution(self, lst):
        max_profit=0
        for i in range(len(lst)-1):
            for j in range(i, len(lst)):
                if lst[j]-lst[i] > max_profit:
                    max_profit = lst[j]-lst[i]

        return max_profit

    def better_solution(self, lst):
        max_profit = 0
        peak = lst[0]
        valley = lst[0]

        for i in range(1, len(lst)-1):
            if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
                peak = max(peak, lst[i])
            elif lst[i] < lst[i-1] and lst[i] < lst[i+1]:
                if valley >=  lst[i]:
                    max_profit = max(peak - valley, max_profit)
                    valley = lst[i]
                    peak = lst[i]

        return max(peak-valley, lst[-1]-valley)

    def best_solution(self, lst):
        max_profit = 0
        current_highest = 0
        for i in reversed(lst):
            max_profit = max(max_profit, current_highest-i)
            current_highest = max(current_highest, i)

        return max_profit