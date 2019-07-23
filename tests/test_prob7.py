from src.prob7 import Solution

def test_prob7_1():
    s = Solution()
    assert s.solution("") == 1

def test_prob7_2():
    s = Solution()
    assert s.solution("1") == 1

def test_prob7_3():
    s = Solution()
    assert s.solution("11") == 2

def test_prob7_4():
    s = Solution()
    assert s.solution("111") == 3

def test_prob7_5():
    s = Solution()
    assert s.solution("1111") == 5

def test_prob7_6():
    s = Solution()
    assert s.solution("3333") == 1

