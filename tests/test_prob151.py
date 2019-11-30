from src.prob151 import Solution

def test_prob151_1():
    s = Solution([["B","B","W"],["W","W","W"],["W","W","W"],["B","B","B"]])
    s.solution((2,2), "G")
    assert s.array == [["B","B","G"],["G","G","G"],["G","G","G"],["B","B","B"]]
