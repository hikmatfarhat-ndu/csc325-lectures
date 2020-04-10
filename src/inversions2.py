import numpy as np
import argparse
from random import shuffle

parser=argparse.ArgumentParser()
parser.add_argument('--num_passes',help="number of passes of radix sort",default=3,type=int)
args=parser.parse_args()


input=np.random.randint(1,1000,10)
a=[3,9,17]
b=[4,5,13]

def brute_force(A):
   n=len(A)
   count=0
   for i in range(1,len(A)):
      for j in range(0,i):
         if A[i]<A[j]:
            count+=1
   return count


def merge(a,b):
   c=np.array([-1 for i in range(len(a)+len(b))])
   j,k=0,0
   count=0
   for i,v in enumerate(c):
      if j==len(a):
         c[i]=b[k]
         k+=1
      elif k==len(b):
         c[i]=a[j]
         j+=1
      elif a[j]<= b[k]:
         c[i]=a[j]
         j+=1
      else:
         c[i]=b[k]
         count+=(len(a)-j)
         k+=1
   return c,count

def merge_sort(A,s,e):
   if s==e:
      return [A[s]],0
   m=int((s+e)/2)

   x,c1=merge_sort(A,s,m)
   y,c2=merge_sort(A,m+1,e)
   z,c3=merge(x,y)
   return z,c1+c2+c3
for i in range(1):

   input=np.random.randint(1,1000,8)
   print("input is {}".format(input))
   z,c=merge_sort(input,0,len(input)-1)
   print("count={} sorted {}".format(c,z))

