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

    def __str__(self):
        string = "An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index. If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses."
        return string

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

    def get(self, idx):
        """
        Get Node obj at idx.
        pre: idx < list length
        Args:
            idx: int
        Returns:
            Node at idx
        """
        curr = self.head

        while curr.next and idx > 0:
            curr = curr.next
            idx -= 1

        return curr


