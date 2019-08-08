from src.prob41 import Solution

def test_prob41_1():
    s = Solution()
    assert s.solution([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL') == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

def test_prob41_2():
    s = Solution()
    assert s.solution([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A') == ['A', 'B', 'C', 'A', 'C']

def test_prob41_3():
    s = Solution()
    assert s.solution([('SFO', 'COM'), ('COM', 'YYZ')], 'COM') == None 