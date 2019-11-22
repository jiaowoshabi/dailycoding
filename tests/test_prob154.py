from src.prob154 import Stack

def test_prob154_1():
    s = Stack()
    s.push("write spec")
    s.push("create tests")
    s.push("write code")
    s.push("release product")

    assert s.pop() == "release product"
    assert s.pop() == "write code"
    assert s.pop() == "create tests"
    assert s.pop() == "write spec"
