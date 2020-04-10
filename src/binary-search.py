import numpy as np
# the find function below
# just iterates over all elements
# so it is \Theta(n)
def find(A,x):
    for v in A:
        if v==x:
            return True

    return False



#binary search function
def bs(A,s,e,x):
    if s>=e:
        if x==A[s]:
            return True
        else:
            return False
    m=int((s+e)/2)
    if x==A[m]:
        return True
    elif x<A[m]:
        return bs(A,s,m-1,x)
    else:
        return bs(A,m+1,e,x)



input=np.random.randint(0,50,32)
x=(np.random.randint(0,50,1))[0]
y=input.copy()
y.sort()
print("x={} and brute={}".format(x,find(input,x)))
print("{}".format(input))
print(bs(y,0,len(y)-1,x))
