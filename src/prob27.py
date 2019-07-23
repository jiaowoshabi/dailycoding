class Solution:
    def __init__(self):
        self.dic = dict()
        self.dic["("] = ")"
        self.dic["["] = "]"
        self.dic["{"] = "}"


    def __str__(self):
        string = "Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed)."
        return string

    def solution(self, string):
        stack = list()

        for i in string:
            if i in ("(", "[", "{"):
                stack.append(i)
            elif i in (")", "]", "}"):
                o = stack.pop()
                if i != self.dic[o]:
                    return False 

        return len(stack) == 0