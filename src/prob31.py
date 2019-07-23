class Solution:
    def __init__(self):
        pass

    def __str__(self):
        string = "The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”. Given two strings, compute the edit distance between them."
        return string

    def solution(self, s1, s2):
        if s1 is None or len(s1)==0:
            return len(s2)
        elif s2 is None or len(s2)==0:
            return len(s1)

        if s1[0] != s2[0]:
            return 1 + min(self.solution(s1[0:], s2[1:]), self.solution(s1[1:], s2[1:]), self.solution(s1[1:], s2[0:]))

        return self.solution(s1[1:], s2[1:])