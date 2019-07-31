from src.prob40 import Solution

def test_prob40_1():
    s = Solution()
    assert s.solution1([6, 1, 3, 3, 3, 6, 6]) == 1
    assert s.solution1([13, 19, 13, 13]) == 19


def test_prob40_1():
    s = Solution()
    assert s.solution2([6, 1, 3, 3, 3, 6, 6]) == 1
    assert s.solution2([13, 19, 13, 13]) == 19