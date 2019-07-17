class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

class Solution:
    def __init__(self):
        pass

    def __str__(self):
        string = "Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list. The list is very long, so making more than one pass is prohibitively expensive."
        return string

    def solution(self, node, k):
        fast = node
        slow = node
        while (k != 0) :
            fast = fast.nxt
            k -= 1

        while fast:
            fast = fast.nxt
            slow = slow.nxt

        return slow