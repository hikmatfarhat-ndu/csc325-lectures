import numpy as np

# def partition(array, begin, end):
#     pivot = begin
#     for i in xrange(begin+1, end+1):
#         if array[i] <= array[begin]:
#             pivot += 1
#             array[i], array[pivot] = array[pivot], array[i]
#     array[pivot], array[begin] = array[begin], array[pivot]
#    return pivot
def partition(a,p,r):
    x=a[r]
    i=p-1
    for j in range(p,r+1):
        if(a[j]<=x):
            i+=1
            a[i],a[j]=a[j],a[i]

    a[i],a[r]=a[r],a[i]
    return i

def quicksort(a,p,r):
     def _quicksort(a,p,r):
         if(p>=r):
             return
         q=partition(a,p,r)
         _quicksort(a,p,q-1)
         _quicksort(a,q+1,r)
     return _quicksort(a,p,r)


    
    
