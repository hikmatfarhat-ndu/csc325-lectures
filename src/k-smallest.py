import numpy as np
import partition

# random.randint(x,y) returns a random
#integer drawn from the interval [x,y)


def select(A,s,e,k):
# there is no need for the base case
# the base case is reached in the elif case
    p=np.random.randint(s,e+1)
    val=A[p]
    i,j=partition.part(A,s,e,p)

    if k <=i-s+1:
        return select(A,s,i,k)
    elif k<=i-s+e-j+2:
        return val
    else:
        return  select(A,i+1,j-1,k-i+s-e+j-2)

input_size=30
for i in range(10):
    k=np.random.randint(1,30)
    input=np.random.randint(1,2*input_size,input_size)
    x=select(input,0,len(input)-1,k)
    
    input.sort()
    
    if x!= input[k-1]:
        print("error")
        print(x)
        print(input[k-1])
        print(input)
    else:
        print("the {} smallest is {}".format(k,x))
        print(" in {}".format(input))
        print("correct")

    print("------")
