from src.prob23 import Solution

def test_prob23_1():
    s = Solution()
    board = [[False, False, False, False], 
            [True, True, False, True], 
            [False, False, False, False],
            [False, False, False, False]]
    start = (3,0)
    end = (0,0)
    assert s.solution(board, start, end) == 7

def test_prob23_2():
    s = Solution()
    board = [[False, False, False, False], 
            [True, True, False, True], 
            [True, True, True, True],
            [False, False, False, False]]
    start = (3,0)
    end = (0,0)
    assert s.solution(board, start, end) == None

