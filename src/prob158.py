class Solution:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def solution(self, array):
        def helper(array, row, col):
            if row == len(array)-1 and col == len(array[0])-1:
                return 1
            elif array[row][col] == 1:
                return 0
            if row + 1 < len(array) and col + 1 < len(array[0]):
                return helper(array, row+1, col) + helper(array, row, col+1)
            elif row + 1 < len(array):
                return helper(array, row+1, col)
            elif col + 1 < len(array[0]):
                return helper(array, row, col+1)
        return helper(array, 0, 0)