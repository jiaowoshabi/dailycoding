def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

class Solution:
    def __init__(self):
        pass

    def __str__(self):
        string = "cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4."
        return string

    def car(self, f):
        def first(a, b):
            return a
        return f (first)

    def cdr(self, f):
        def second(a, b):
            return b
        return f (second)