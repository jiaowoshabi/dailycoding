class Solution:
    def __init__(self):
        self.cache = dict()

    def __str__(self):
        string = "The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”. Given two strings, compute the edit distance between them."
        return string

    def solution(self, s1, s2, t1=None, t2=None, t3=None, t4=None):
        if s1 is None or len(s1)==0:
            self.cache[(s1,s2)] = len(s2)
            return self.cache[(s1,s2)]
        elif s2 is None or len(s2)==0:
            self.cache[(s1,s2)] = len(s1)
            return self.cache[(s1,s2)]

        if s1[0] != s2[0]:
            if (s1[0:], s2[1:]) in self.cache:
                t1 = self.cache[(s1[0:], s2[1:])]
            else:
                t1 = self.solution(s1[0:], s2[1:])
                self.cache[(s1[0:], s2[1:])] = t1
            if (s1[1:], s2[1:]) in self.cache:
                t2 = self.cache[(s1[1:], s2[1:])]
            else:
                t2 = self.solution(s1[1:], s2[1:])
                self.cache[(s1[1:], s2[1:])] = t2
            if (s1[1:], s2[0:]) in self.cache:
                t3 = self.cache[(s1[1:], s2[0:])]
            else:
                t3 = self.solution(s1[1:], s2[0:])
                self.cache[(s1[1:], s2[0:])] = t3

            return 1 + min(t1, t2, t3)

        if (s1[1:], s2[1:]) in self.cache:
            return self.cache[(s1[1:], s2[1:])]
        self.cache[(s1[1:], s2[1:])] = self.solution(s1[1:], s2[1:])

        return self.cache[(s1[1:], s2[1:])]