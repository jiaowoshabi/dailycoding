from src.prob47 import Solution

def test_prob47_1():
    s = Solution()
    assert s.solution([9, 11, 8, 5, 7, 10]) == 5

def test_prob47_2():
    s = Solution()
    assert s.better_solution([9, 11, 8, 5, 7, 10]) == 5

def test_prob47_3():
    s = Solution()
    assert s.better_solution([1,4,3,5]) == 4


def test_prob47_4():
    s = Solution()
    assert s.better_solution([1,4]) == 3

def test_prob47_5():
    s = Solution()
    assert s.better_solution([4,3]) == 0

def test_prob47_6():
    s = Solution()
    assert s.best_solution([1,4,3,5]) == 4


def test_prob47_7():
    s = Solution()
    assert s.best_solution([1,4]) == 3

def test_prob47_8():
    s = Solution()
    assert s.best_solution([4,3]) == 0