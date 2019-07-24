import numpy as np

class  Solution(object):
    """docstring for  Solution"""
    def __init__(self):
        pass

    def __str__(self):
        string = "Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.Recall that the median of an even-numbered list is the average of the two middle numbers."
        return string
        
    def solution1(self, lst):
        ret = list()
        for i in range(0, len(lst)):
            median = np.median(lst[0:i+1])
            ret.append(median)

        return ret

    