from src.prob26 import Node, Solution

def test_prob26_1():
    s = Solution()
    n1 = Node("foo")
    n2 = Node("bar")
    n3 = Node("foo_bar")
    n4 = Node("bar_foo")
    n1.nxt = n2
    n2.nxt = n3
    n3.nxt = n4

    assert s.solution(n1, 1).val == "bar_foo"
    assert s.solution(n1, 2).val == "foo_bar"
    assert s.solution(n1, 3).val == "bar"
    assert s.solution(n1, 4).val == "foo"