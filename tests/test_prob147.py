from src.prob147 import Solution
from src.utils import ListNode

def test_prob146_1():
    s = Solution()

    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(2)
    d = ListNode(6)
    e = ListNode(5)
    f = ListNode(8)

    # list1
    list1= a
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    res = s.solution(list1, 1, 4)

    assert res.val == 1
    assert res.next.val == 5
    assert res.next.next.val == 6
    assert res.next.next.next.val == 2
    assert res.next.next.next.next.val == 3
    assert res.next.next.next.next.next.val == 8

def test_prob146_2():
    s = Solution()

    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(2)
    d = ListNode(6)
    e = ListNode(5)
    f = ListNode(8)

    # list1
    list1= a
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    res = s.solution(list1, 1, 3)

    assert res.val == 1
    assert res.next.val == 6
    assert res.next.next.val == 2
    assert res.next.next.next.val == 3
    assert res.next.next.next.next.val == 5
    assert res.next.next.next.next.next.val == 8