from src.prob145 import Solution
from src.utils import ListNode

def test_prob145_1():
    s = Solution()

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)

    # list1
    list1= a
    a.next = b
    b.next = c
    c.next = d


    list2 = s.solution(list1)

    assert list2.val == 2
    assert list2.next.val == 1
    assert list2.next.next.val == 4
    assert list2.next.next.next.val == 3

def test_prob145_2():
    s = Solution()

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)

    # list1
    list1= a
    a.next = b
    b.next = c


    list2 = s.solution(list1)

    assert list2.val == 2
    assert list2.next.val == 1
    assert list2.next.next.val == 3