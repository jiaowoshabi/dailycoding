from src.prob33 import Solution

def test_prob33_1():
    s = Solution()
    assert s.solution1([2, 1, 5, 7, 2, 0, 5]) == [2.0, 1.5, 2.0, 3.5, 2.0, 2.0, 2.0]

def test_prob33_2():
    s = Solution()
    assert s.solution1([]) == []
