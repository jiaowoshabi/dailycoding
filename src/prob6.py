"""
Questions: what if the doubly linked list allows cycle?
"""
class XORNode:
    def __init__(self, val, prev=-1, next=-1):
        """
        Args:
            val: node value
            prev: address of the previous node; -1 denotes addr of None
            next: address of the next node; -1 denotes addr of None
        """
        self.val = val
        self.both = prev ^ next

class Solution_XOR:
    def __init__(self, head):
        self.memory = [XORNode(head)]


    def __str__(self):
        string = "An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index. If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses."
        return string

    def add(self, val):
        """
        Adds a node contains val at the end of the doubly linked list
        Args:
            val; value of a node which will be added at the end
        Return:
            the head of the list
        """
        prev, curr = -1, self.memory[0]
        while (curr.both ^ prev) != -1:
            next_addr = curr.both ^ prev
            prev = self.get_pointer(curr)
            curr = self.dereference_pointer(next_addr)

        new_node = XORNode(val, self.get_pointer(curr), -1)
        self.memory.append(new_node)
        curr.both = prev ^ self.get_pointer(new_node)

        return self.memory[0]

    def get(self, idx):
        """
        Get Node obj at idx.
        pre: idx < list length
        Args:
            idx: int
        Returns:
            Node at idx
        """
        prev, curr = -1, self.memory[0]

        while (curr.both ^ prev) != -1 and idx > 0:
            next_addr = curr.both ^ prev
            prev = self.get_pointer(curr)
            curr = self.dereference_pointer(next_addr)
            idx -= 1

        return curr

    def get_pointer(self, node):
        return self.memory.index(node)

    def dereference_pointer(self, idx):
        return self.memory[idx]