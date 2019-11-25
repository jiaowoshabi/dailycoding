class Solution:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def solution(self, string):
        lookup = set()
        for i in string:
            if i in lookup:
                lookup.remove(i)
            else:
                lookup.add(i)
        return len(lookup) <= 1


