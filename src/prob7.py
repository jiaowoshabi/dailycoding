from collections import defaultdict

class Solution:
    def __init__(self):
        pass


    def __str__(self):
        string = "Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded. For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.You can assume that the messages are decodable. For example, '001' is not allowed."
        return string

    def solution(self, string):
        """Dynamic Programming solution
        Define OPT(str) as the optimal solution, which denotes the number of ways of decoding. Recursion using bottom up:

        * Base case: OPT("x") = 1 or OPT("") = 1
        * Recurisve case:
            The OPT(string) = 1) + 2)
            1) if the first two letters of current string is a letter, then # of ways of decoding is OPT(string[2:]) 
            2) # of ways of decoding is OPT(strring[1:])
        """
        cache = defaultdict(int)
        cache[len(string)] = 1
        
        for i in reversed(range(len(string))):
            if string[i].startswith("0"):
                cache[i] = 0
            elif i == len(string) - 1:
                cache[i] = 1
            else:
                if int(string[i:i+2]) <= 26:
                    cache[i] += cache[i+2]
                cache[i] += cache[i+1]

        return cache[0]
