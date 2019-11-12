from src.prob144 import Solution

def test_prob144_1():
    s = Solution()

    assert s.solution([4,1,3,5,6], 0) == 3
    assert s.solution([4,3,2,1], 0) == None
    assert s.solution([1,2,3,4], 3) == None
    assert s.solution([4], 0) == None
    assert s.solution([], 0) == None
    assert s.solution([4,1,3,6,5,9], 3) == 5
    assert s.solution([7,3,6,5,9], 2) == 4


def test_prob144_2():
    s = Solution()

    assert s.better_solution([4,1,3,5,6], 0) == 3
    assert s.better_solution([4,3,2,1], 0) == None
    assert s.better_solution([1,2,3,4], 3) == None
    assert s.better_solution([4], 0) == None
    assert s.better_solution([], 0) == None
    assert s.better_solution([4,1,3,6,5,9], 3) == 5
    assert s.better_solution([7,3,6,5,9], 2) == 4