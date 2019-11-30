from src.prob143 import Solution

def test_prob143_1():
    s = Solution()

    assert s.solution([9, 12, 3, 5, 14, 10, 10], 10) == [9, 3, 5, 10, 10, 12, 14]

def test_prob144_1():
    s=Solution()
    assert s.better_solution([9, 12, 3, 5, 14, 10, 10], 10) == [9, 3, 5, 10, 10, 12, 14]


