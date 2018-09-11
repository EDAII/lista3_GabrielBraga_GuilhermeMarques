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

    def shellSort(self, l):
        n = len(l)
        gap = n/2
        
        while gap > 0:
            for i in range(gap,n):
                tmp = l[i]
                j = i
                while j >= gap and l[j-gap] > tmp:
                    l[j] = l[j-gap]
                    j -= gap
                    l[j] = tmp
            gap = gap/2
    
    def merge(self, lst, left, mid, right): 
        n1 = mid - left + 1
        n2 = right - mid 
   
        L = [0] * (n1) 
        R = [0] * (n2) 
    
        for i in range(0 , n1): 
            L[i] = lst[left + i] 
  
        for j in range(0 , n2): 
            R[j] = lst[mid + 1 + j] 
  
        i = 0   
        j = 0    
        k = left     
  
        while i < n1 and j < n2 : 
            if L[i] <= R[j]: 
                lst[k] = L[i] 
                i += 1
            else: 
                lst[k] = R[j] 
                j += 1
            k += 1
  
        while i < n1: 
            lst[k] = L[i] 
            i += 1
            k += 1

        while j < n2: 
            lst[k] = R[j] 
            j += 1
            k += 1

    def mergeSort(self,lst,left,right): 
        if left < right: 
            mid = (left+(right-1))/2
            self.mergeSort(lst, left, mid) 
            self.mergeSort(lst, mid+1, right) 
            self.merge(lst, left, mid, right) 
        
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
    
    def insertion_sort(list):

    for x in range(0, len(list)):
        y = x
        while ((y != 0) and (list[y] < list[y-1])):
            aux = list[y]
            list[y] = list[y-1]
            list[y-1] = aux
            y -= 1
    return list

    def hashing(self, lst):
        m = lst[0]
        for i in range(1,len(lst)):
            if(m < lst[i]):
                m = lst[i]
        result = [m,int(math.sqrt(len(lst)))]
        return result
    
    def re_hashing(self, i, code):
        return int(i/code[0]*(code[1]-1))

    def bucketSort(self, lst):
        code = hashing(lst)
        buckets = [list() for _ in range(code[1])]
        for i in lst:
            x = re_hashing(i, code)
            buck = buckets[x]
            buck.append(i)
        for bucket in buckets:
            self.insertion_sort(bucket)
        ndx = 0
        for b in range(len(buckets)):
            for v in buckets[b]:
                lst[ndx] = v
                ndx +=1

