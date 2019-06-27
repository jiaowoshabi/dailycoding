from src.prob6 import Solution, Node, XNode

def test_prob6_1():
    s = Solution(Node("foo"))

    assert s.head.val == "foo"
    assert s.add(Node("bar")).val == "foo"
    assert s.head.next.val == "bar"
    assert s.head.next.prev.val == "foo"