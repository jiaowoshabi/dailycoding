class Solution:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def solution(self, lst):
        """
        Time: O(n^2)
        Space: O(n)
        """
        unique = set(lst)

        max_occ = 1
        curr_num = lst[0]
        for i in unique:
            count = lst.count(i)
            if count > max_occ:
                max_occ = count
                curr_num = i
        return curr_num

    def better_solution(self, lst):
        """
        Divide and Conquer
        (majority, count) in left ? (majority, count) in right
        """
        def helper(lst, left, right):
            if left + 1 == right:
                return lst[left], 1

            mid = int((left + right)/2)
            left_maj, left_count = helper(lst, left, mid)
            right_maj, right_count = helper(lst, mid, right)

            if left_maj == right_maj:
                return left_maj, left_count+right_count

            left_maj_count = lst[mid:right].count(left_maj) + left_count
            right_maj_count  = lst[left:mid].count(right_maj) + right_count

            if left_maj_count >= right_maj_count:
                return left_maj, left_maj_count
            else:
                return right_maj, right_maj_count

        res, _ = helper(lst, 0, len(lst))
        return res

