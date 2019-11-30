from src.prob149 import Solution

def test_prob149_1():
    s = Solution()
    assert [(0, 0), (3, 1)] == s.solution([(0, 0), (5, 4), (3, 1)], (1, 2), 2)

