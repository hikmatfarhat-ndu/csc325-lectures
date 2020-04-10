# Quick Sort
import random
def printArray(arr):
  print (' '.join(str(i) for i in arr))


def quicksort(arr, i, j):
  if i < j:
    pos = partition(arr, i, j)
    quicksort(arr, i, pos - 1)
    quicksort(arr, pos + 1, j)


def partition(A, s, e):
  pivot = A[e]
  i = s - 1
  for j in range(s, e):
    if A[j] <= pivot:
      i += 1
      A[i],A[j]=A[j],A[i]

  A[e],A[i+1]=A[i+1],A[e]

  return i + 1


#arr = [9, 4, 8, 3, 1, 2, 5]
arr=[random.randint(0,30) for y in range(0,10)]
print ("Initial Array :{}".format(arr))
quicksort(arr, 0, len(arr) - 1)
print("sorted Array: {}".format(arr))



