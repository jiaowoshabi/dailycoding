from src.prob31 import Solution

def test_prob31_1():
    s = Solution()
    assert s.solution("kitten", "sitting") == 3

def test_prob31_2():
    s = Solution()
    assert s.solution("kitten", "") == 6

def test_prob31_3():
    s = Solution()
    assert s.solution("ab", "b") == 1

def test_prob31_4():
    s = Solution()
    assert s.solution("bab", "ab") == 1
