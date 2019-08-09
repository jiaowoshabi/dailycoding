"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""
from collections import deque
class Solution:
    def __init__(self):
        pass

    def solution(self, lst):
        depths = []
        queue = deque()
        sorted_intervals = sorted(lst, key=lambda t: t[0])
        queue.append(sorted_intervals[0])

        depth = 1
        for interval in sorted_intervals[1:]:
            head = queue[0]
            # compare the starting time of interval with the ending time of head
            if head[1] >= interval[0]:
                depth += 1
                queue.append(interval)
            else:
                queue.popleft()

            depths.append(depth)

        return max(depths)
            

