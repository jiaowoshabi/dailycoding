from src.prob1 import Solution

def test_prob1_1():
    s = Solution()
    assert s.two_sum([10,5,6,7], 17) == True
    assert s.better_two_sum([10,5,6,7], 17) == True

def test_prob1_2():
    s = Solution()
    assert s.two_sum([], 17) == False
    assert s.better_two_sum([], 17) == False

def test_prob1_3():
    s = Solution()
    assert s.two_sum([10], 10) == False
    assert s.better_two_sum([10], 10) == False

def test_prob1_4():
    s = Solution()
    assert s.two_sum([10,5,6,10], 20) == True
    assert s.better_two_sum([10,5,6,10], 20) == True

def test_prob1_5():
    s = Solution()
    assert s.two_sum([10,5,6,11], 20) == False
    assert s.better_two_sum([10,5,6,11], 20) == False

