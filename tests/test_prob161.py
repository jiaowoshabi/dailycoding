from src.prob161 import Solution

def test_prob161_1():
    s = Solution()
    assert 268435456 == s.solution(8)
    assert 3758096384== s.solution(7)
    assert 0== s.solution(0)