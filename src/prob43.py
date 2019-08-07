class Solution(object):
    def __init__(self):
        self.stack = list()
        self.max_curr = list()

    def __str__(self):
        string = ""
        return string

    def push(self, val):
        self.stack.append(val)
        if self.max_curr and self.max_curr[-1] < val:
            self.max_curr.append(val)
        elif not self.max_curr:
            self.max_curr.append(val)

    def pop(self):
        if self.stack:
            out = self.stack.pop()
            if out == self.max_curr[-1]:
                self.max_curr.pop()
            return out
        else:
            raise ValueError("Empty stack, cannot do pop op")

    def max(self):
        if self.max_curr:
            return self.max_curr[-1]
        return None

