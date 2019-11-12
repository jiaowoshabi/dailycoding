from src.prob34 import Solution

def test_prob34_1():
    s = Solution()
    assert s.n_solution("google") == "elgoogle"

def test_prob34_2():
    s = Solution()
    assert s.n_solution("race") == "ecarace"

def test_prob34_3():
    s = Solution()
    assert s.top_bottom("google") == "elgoogle"

def test_prob34_4():
    s = Solution()
    assert s.top_bottom("race") == "ecarace"

def test_prob34_5():
    s = Solution()
    assert s.bottom_up("google") == "elgoogle"

def test_prob34_6():
    s = Solution()
    assert s.bottom_up("race") == "ecarace"

