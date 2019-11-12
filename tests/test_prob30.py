from src.prob30 import Solution

def test_prob30_1():
    s = Solution()
    assert s.my_solution([3,0,1,3,0,5]) == 8
    assert s.my_solution([1,2,3]) <= 0
    assert s.my_solution([2,1,3]) == 1

def test_prob30_2():
    s = Solution()
    assert s.better_solution([3,0,1,3,0,5]) == 8
    assert s.better_solution([1,2,3]) <= 0
    assert s.better_solution([2,1,3]) == 1