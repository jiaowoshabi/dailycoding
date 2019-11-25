from src.prob155 import Solution

def test_prob155_1():
    s = Solution()
    assert 1 == s.solution([1, 2, 1, 1, 3, 4, 0])

def test_prob155_2():
    s = Solution()
    assert 1 == s.better_solution([1, 2, 1, 1, 3, 4, 0])

def test_prob155_3():
    s = Solution()
    assert 2 == s.better_solution([2])

def test_prob155_4():
    s = Solution()
    assert 2 == s.better_solution([1, 2, 2, 2])