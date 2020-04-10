import numpy as np

def swap(A,x,y):
    tmp=A[x]
    A[x]=A[y]
    A[y]=tmp

#partition the array where
#s is the starting index
#e the ending index
#m the index of the pivot

def part(A,s,e,m):
    i,k,j=s-1,s,e
#put the pivot at the end
    swap(A,m,e)
    pivot=A[e]
    while k <j:
        if A[k]>pivot:
            k+=1
        elif A[k]<pivot:
            i+=1
            swap(A,i,k)
            k+=1
        else:
            j=j-1
            swap(A,k,j)
    return i,j


