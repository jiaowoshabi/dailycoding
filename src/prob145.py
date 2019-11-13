class Solution:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def solution(self, head):
        curr = head

        while curr and curr.next:
            curr.val, curr.next.val = curr.next.val, curr.val
            curr = curr.next.next

        return head
        


    def better_solution(self, lst, head):
        pass