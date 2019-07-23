from src.prob27 import Solution

def test_prob27_1():
    s = Solution()
    assert s.solution("")
    assert s.solution("([])[]({})")
    assert not s.solution("([)]")
    assert not s.solution("((()")