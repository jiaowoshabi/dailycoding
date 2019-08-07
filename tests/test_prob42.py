from src.prob42 import Solution

def test_prob42_1():
    s = Solution()

    assert set(s.solution([12, 1, 61, 5, 9, 2], 24)) == set([12, 1, 9, 2])

def test_prob42_2():
    s = Solution()

    assert set(s.interative_sol([12, 1, 61, 5, 9, 2], 24)) == set([12, 1, 9, 2])