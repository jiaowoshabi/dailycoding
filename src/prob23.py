from collections import deque
class Solution:
    def __init__(self):
        pass

    def solution(self, matrix, start, end):
        def walkable(matrix, row, col):
            if row < 0 or row >= len(matrix):
                return False
            elif col < 0 or col >= len(matrix[0]):
                return False
            return not matrix[row][col]

        def get_neighbors(matrix, row, col):
            return [(r, c) for r, c in [(row-1, col), 
                                        (row+1, col), 
                                        (row, col+1), 
                                        (row, col-1)] if walkable(matrix, r, c)]

        queue = deque([(start, 0)])
        seen = set()
        while queue:
            cord, count = queue.popleft()
            seen.add(cord)
            if cord == end:
                return count
            for neighbor in get_neighbors(matrix, cord[0], cord[1]):
                if neighbor not in seen:
                    queue.append((neighbor,count+1))