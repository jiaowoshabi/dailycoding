class Solution:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        pass

    def solution(self, loc, target):
        
        def helper(loc, target, color):
            """
            loc is a tuple
            """
            row = loc[0]
            col = loc[1]
            if row >= len(self.array) or row < 0:
                return
            elif col >= len(self.array[0]) or col < 0:
                return
            elif self.array[row][col] != color:
                return

            # change the current loc color
            self.array[row][col] = target

            # if this loc has the same  color as given, then explore its neighbors
            # left
            helper((row, col-1), target, color)
            # right
            helper((row, col+1), target, color)
            # up
            helper((row-1, col), target, color)
            # down
            helper((row+1, col), target, color)

            return
        
        row = loc[0]
        col = loc[1]
        helper((row, col), target, self.array[row][col])
        return

