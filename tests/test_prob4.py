import pytest
from src.prob4 import Solution

def test_prob4_1():
    s = Solution()
    assert s.solution([3,4,-1,1]) == 2
    assert s.better_solution([3,4,-1,1]) == 2

def test_prob4_2():
    s = Solution()
    assert s.solution([1,2,0]) == 3
    assert s.better_solution([1,2,0]) == 3

def test_prob4_3():
    s = Solution()
    assert s.solution([]) == 1
    assert s.better_solution([]) == 1