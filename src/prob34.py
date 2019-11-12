class Solution:
    def __init__(self):
        self.cache = {}

    def is_palindrome(self, string):
        return string == string[::-1]

    def n_solution(self, string):
        if self.is_palindrome(string):
            return string

        if string[0] == string[-1]:
            return string[0] + self.n_solution(string[1:-1]) + string[-1]
        else:
            pivot_left = string[0]+self.n_solution(string[1:])+string[0]
            pivot_right = string[-1]+self.n_solution(string[:-1])+string[-1]
            
            if len(pivot_left) == len(pivot_right):
                return min(pivot_left, pivot_right)
            
            return min(pivot_left, pivot_right, key=lambda x: len(x))

    def top_bottom(self, string):
        if string in self.cache:
            return cache[string]

        if self.is_palindrome(string):
            self.cache[string] = string
            return string

        if string[0] == string[-1]:
            res = string[0] + self.n_solution(string[1:-1]) + string[-1]
            self.cache[s] = res
            return self.cache[s]
        else:
            pivot_left = string[0]+self.n_solution(string[1:])+string[0]
            pivot_right = string[-1]+self.n_solution(string[:-1])+string[-1]
            
            if len(pivot_left) == len(pivot_right):
                res = min(pivot_left, pivot_right)
                self.cache[string] = res
                return res
            
            res = min(pivot_left, pivot_right, key=lambda x: len(x))
            self.cache[string] = res
            return res

    def bottom_up(self, string):
        if len(string) <= 1:
            return string

        table = [[""] * (len(string)+1) for _ in range(len(string)+1)]

        for i in range(len(string)):
            table[i][1] = string[i]

        for j in range(2, len(string)+1):
            for i in range(len(string)-j+1):
                term = string[i:i+j]
                first = term[0]
                last = term[-1]
                if first == last:
                    table[i][j] = first + table[i+1][j-2] + last
                else:
                    pivot_left = first + table[i+1][j-1] + first
                    pivot_right = last + table[i][j-1] + last

                    if len(pivot_left) == len(pivot_right):
                        table[i][j] = min(pivot_left, pivot_right)
            
                    else:
                        table[i][j] = min(pivot_left, pivot_right, key=lambda x: len(x))

        return table[0][-1]

