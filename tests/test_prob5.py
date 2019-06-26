from src.prob5 import Solution, cons

def test_prob5_1():
    s = Solution()
    assert s.car(cons(3,4)) == 3
    assert s.cdr(cons(3,4)) == 4