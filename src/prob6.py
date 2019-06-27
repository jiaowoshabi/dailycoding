"""
Questions: what if the doubly linked list allows cycle?
"""
class XNode:
    def __init__(self, val, both=0):
        self.val = val
        self.both = both

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def __init__(self, head):
        self.head = head

    def add(self, node):
        """
        Adds a node contains element at the end of the doubly linked list
        Args:
            node; Node instance to be added at the end
        Return:
            the head of the list
        """
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = node
        node.prev = curr

        return self.head

    def get(self, index):
