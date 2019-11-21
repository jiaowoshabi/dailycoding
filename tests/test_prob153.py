from src.prob153 import Solution

def test_prob146_1():
    s = Solution()
    assert s.solution("hello", "world", "dog cat hello cat dog dog hello cat world") == 1

    assert s.solution("hello", "world", "dog cat hello cat dog dog hello cat dog dog world") == 3
    assert s.solution("hello", "world", "dog cat hello cat dog dog hello cat") == 8

def test_prob146_2():
    s = Solution()
    assert s.better_solution("hello", "world", "dog cat hello cat dog dog hello cat world") == 1

    assert s.better_solution("hello", "world", "dog cat hello cat dog dog hello cat dog dog world") == 3
    assert s.better_solution("hello", "world", "dog cat hello cat dog dog hello cat") == float('inf')
