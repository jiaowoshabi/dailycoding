class Solution:
    def __init__(self):
        pass


    def __str__(self):
        string = "Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded. For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.You can assume that the messages are decodable. For example, '001' is not allowed."
        return string

    def solution(self, string):
        """Dynamic Programming solution
        Define OPT(str) as the optimal solution, which denotes the number of ways of decoding. Recursion using bottom up:

        * Base case: OPT("x") = 1
        * Recurisve case:
            Every time a new letter, ``curr`` is added. There can only be 2 cases:
            * if ``prev+curr`` can form a new letter, then OPT(str+curr) = OPT(str)+1
            * otherwise, OPT(str+curr) = OPT(str)
        """
        if string.startswith("0"):
            return 0
        elif len(string) <= 1:
            return 1
        
        total = 0

        if int(string[:2]) <= 26:
            total += self.solution(string[2:])

        total += self.solution(string[1:])

        return total
