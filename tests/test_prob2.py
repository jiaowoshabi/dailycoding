import pytest
from src.prob2 import Solution

def test_prob2_1():
    s = Solution()
    assert s.solution([1,2,3,4,5]) == [120, 60, 40, 30, 24]
    assert s.no_div([1,2,3,4,5]) == [120, 60, 40, 30, 24]
    assert s.better_solution([1,2,3,4,5]) == [120, 60, 40, 30, 24]

def test_prob2_2():
    s = Solution()
    assert s.solution([3, 2, 1]) == [2,3,6]
    assert s.no_div([3, 2, 1]) == [2,3,6]  
    assert s.better_solution([3, 2, 1]) == [2,3,6]

def test_prob2_3():
    s = Solution()
    assert s.solution([]) == [] 
    assert s.no_div([]) == []
    assert s.better_solution([]) == []

def test_prob2_4():
    s = Solution()
    assert s.solution([2]) == [1] 
    assert s.no_div([2]) == [1]
    assert s.better_solution([2]) == [1]

def test_prob2_5():
    s = Solution()
    with pytest.raises(Exception) as e_info:
        s.solution([3, 2, 1, 0])
    assert s.no_div([3, 2, 1, 0]) == [0,0,0,6]
    assert s.better_solution([3, 2, 1, 0]) == [0,0,0,6]
    

