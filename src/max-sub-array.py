import numpy as np
import argparse
from random import shuffle

parser=argparse.ArgumentParser()
parser.add_argument('--num_passes',help="number of passes of radix sort",default=3,type=int)
args=parser.parse_args()


input=np.random.randint(-20,20,10)
#dynamic programming solution to
#maximum subarray sum
def dynamic(A,e):
   sums=np.zeros(e)
   sums[0]=A[0]
   for i,v in enumerate(sums):
      if i==0:
         sums[0]=A[0]
      else:
         if sums[i-1]<0:
            sums[i]=A[i]
         else:
            sums[i]=sums[i-1]+A[i]

   max=A[0]
   for v in sums:
      if v>max:
         max=v

   return max

def compute_both(A,s,e):
   m=int((s+e)/2)
   sum1,sum2=0,0
   max1=A[m]
   max2=A[m+1]
#from m downto s
   for i in range(m,s-1,-1):
      sum1=sum1+A[i]
      if max1<sum1:
         max1=sum1
#from m+1 upto e
   for i in range(m+1,e+1,1):
      sum2=sum2+A[i]
      if max2<sum2:
         max2=sum2
   return max1+max2

#divide and conquer solution to
#maximum subarray sum

def max_sub_array(A,s,e):
   if s==e:
      return A[s]

   m=int((s+e)/2)
   sum1=max_sub_array(A,s,m)
   sum2=max_sub_array(A,m+1,e)

   sum3=compute_both(A,s,e)

   return max(sum1,sum2,sum3)


x=max_sub_array(input,0,len(input)-1)
