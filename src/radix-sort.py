import numpy as np
import argparse
from random import shuffle

parser=argparse.ArgumentParser()
parser.add_argument('--num_passes',help="number of passes of radix sort",default=3,type=int)
args=parser.parse_args()

w=3
#appends least significant zeros
#so all numbers are 3 digits
def fix(x):
    n=w- len(x)
    if n>0:
     for i in range(n):
       x='0'+x
    return x

input=map(lambda x:str(x),np.random.randint(1,1000,10))
input=map(fix,input)


def one_pass(a,digit):
    x=np.zeros(10,dtype=int)    
    for i,val in enumerate(a):
      index=int( (input[i])[digit])
      x[index]+=1
    for i,val in enumerate(x):
      if i!=0:
         x[i]=x[i]+x[i-1]
    b=[]
    for i in range(10):
        b.append("")

    for i in reversed(a):
        index=int(i[digit])
        x[index]-=1
        b[x[index]]=i
    return b
b=input
num_passes=args.num_passes
for i in range(num_passes):
    b=one_pass(b,w-i-1)
print ("original: {}".format(map(int,input)))
print ("sorted  : {}".format(map(int,b)))
for i in range(4):
 x=map(int,b)
 shuffle(x)
 print ("random  : {}".format(x))
