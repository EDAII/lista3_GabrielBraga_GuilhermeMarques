import time
from math import floor

class Sorter(object):
    def __init__(self):
        pass

    def timer(self, func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        elapsed = end - start

        return (elapsed, result)

    def quicksort(self, l, start, end):
        if start < end:
            i = start
            j = end
            indexPivot = floor((start + end)/2)
            pivot = l[indexPivot]
            while (i < j):
                while (l[i] < pivot):
                    i += 1
                while (l[j] > pivot):
                    j -= 1
                if (i <= j):
                    l[i], l[j] = l[j], l[i]
            self.quicksort(l, start, indexPivot)
            self.quicksort(l, indexPivot+1, end)
