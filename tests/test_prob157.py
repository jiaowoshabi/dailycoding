from src.prob157 import Solution

def test_prob157_1():
    s = Solution()
    assert not s.solution("daily")
    assert s.solution("carrace")