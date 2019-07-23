class Node:
    def __init__(self, val=False, left=None, right=None, parent=None):
        self.is_locked = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution：
    def __init__(self):
        pass


    def __str__(self):
        string = "Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked."
        return string

    def is_locked(self, node):
        return node.is_locked

    def lock(self, node):


    def ancestor_unlocked(self, node):
        if not node:
            return False
        elif not node.parent:
            return True

        return node.parent.is_locked and self.ancestor_unlocked(node.parent)

    def decedents_unlocked(self, node):
        if not node:
            return True
        elif (not node.left) and (not node.right):
            return True
        elif node.left and (not node.right):
            return (node.left.is_locked) == False and self.decedents_unlocked(node.left)
        elif (not node.left) and node.right:
            return (node.right.is_locked) == False and self.decedents_unlocked(node.right)
        return (node.left.is_locked) == False and
               (node.right.is_locked) == False and
               self.decedents_unlocked(node.left) and
               self.decedents_unlocked(node.right) 

    def lock(self, node):
        if not node:
            return False

        if self.ancestor_unlocked(node) or self.decedents_unlocked(node):
            node.is_locked = True

        return False

    def unlock(self, node):
        if not node:
            return False

        if self.ancestor_unlocked(node) or self.decedents_unlocked(node):
            node.is_locked = False

        return False       
