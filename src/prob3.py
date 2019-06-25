from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    """docstring for Solution"""
    def __init__(self):
        pass

    def __str__(self):
        string = "Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree."
        return string

    def serialize(self, root):
        """BFS traverse and serialize bianry tree
        Args:
            root: Node root; root of a binary tree
        Returns:
            A list contains the serialized binary tree.
        """
        if not root:
            return list()

        queue = deque([root])
        ret = []
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                ret.append(None)
        return ret

    def deserialize(self, lst):
        """
        Args:
            lst: serialized binary tree
        Returns:
            deserialized binary tree
        """
        def helper(N, lst):
            root = Node(lst[N])
            if lst[N]:
                root.left = helper(2*N+1, lst)
                root.right = helper(2*N+2, lst)
            return root

        if len(lst) == 0:
            return None

        root = helper(0, lst)
        return root