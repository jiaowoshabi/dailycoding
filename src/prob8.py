class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        pass


    def __str__(self):
        string = "A unival tree (which stands for 'universal value') is a tree where all nodes under it have the same value. Given the root to a binary tree, count the number of unival subtrees."
        return string

    def solution(self):
        pass

    def is_unival(self, root, value):
        if not root:
            return True

        return root.val == is_unival(root.left) and  root.val == root.right

        