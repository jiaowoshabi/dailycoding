class Solution:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def solution(self, string):
        """
        O(n) time complexity, O(n) space complexity
        """
        dic = set()
        for i in string:
            if i in dic:
                return i
            dic.add(i)
        return None

    def better_solution(self, string):
        """
        O(1) space complexity; O(n) time complexity
        """
        arr = [0 for _ in range(128)]

        for char in string:
            i = ord(char)
            if arr[i] == 0:
                arr[i] += 1
            else:
                return char

        return None