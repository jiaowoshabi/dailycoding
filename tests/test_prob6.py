from src.prob6 import Solution_XOR, XORNode

def test_prob6_1():
    s = Solution_XOR("foo")
    assert s.memory[0].val == "foo"
    assert s.add("bar").val == "foo"
    assert s.memory[(s.memory[0].both ^ -1)].val == "bar"

    assert s.add("foo_bar").val == "foo"
    assert s.add("bar_foo").val == "foo"
    assert s.get(0).val == "foo"
    assert s.get(1).val == "bar"
    assert s.get(2).val == "foo_bar"
    assert s.get(3).val == "bar_foo"