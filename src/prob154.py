from time import time
import heapq  

class MaxHeap:
    def __init__(self):
        self._heap = []

    def push(self, item, priority):
        heapq.heappush(self._heap, (-priority, item))

    def pop(self):
        _, item = heapq.heappop(self._heap)
        return item


class Stack:
    def __init__(self):
        self.maxheap = MaxHeap()

    def push(self, item):
        t = time()
        self.maxheap.push(item, t)

    def pop(self):
        return self.maxheap.pop()