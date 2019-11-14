class Solution:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def solution(self, root):
        if root.left is None and root.right is None and int(root.val) == 0:
            return None
        elif root.left is None and root.right is None and int(root.val) == 1:
            return root

        root.left  = self.solution(root.left)
        root.right  = self.solution(root.right)
        if not root.left and not root.right and (root.val) == 0:
            return None
        return root
