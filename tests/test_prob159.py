from src.prob159 import Solution

def test_prob159_1():
    s = Solution()
    assert not s.solution("abcdef")
    assert "b" == s.solution("abbcdef")

def test_prob159_2():
    s = Solution()
    assert not s.better_solution("abcdef")
    assert "b" == s.better_solution("abbcdef")