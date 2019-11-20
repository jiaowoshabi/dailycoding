class Solution:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def solution(self, lst, i, j):
        """
        Time complexity: n = list size; O(n)
        Space complexity: m = j-i; O(m)+O(n)=O(n)
        """
        ptr_array = [None] * (j+1)

        # move slow_ptr pointing to the ith element in the list
        slow_ptr = lst
        for slow_ptr_idx in range(i):
            slow_ptr = slow_ptr.next

        # move fast_ptr pointing to the jth element in the list
        fast_ptr = slow_ptr
        for fast_ptr_idx in range(i,j+1):
            ptr_array[fast_ptr_idx] = fast_ptr
            fast_ptr = fast_ptr.next
            
        # swap values by i++, j-- in interval ptr_array(i, j)
        for dis in range(int((j-i)/2)+1):
            tmp = ptr_array[j-dis].val
            ptr_array[j-dis].val = ptr_array[i+dis].val
            ptr_array[i+dis].val = tmp

        return lst