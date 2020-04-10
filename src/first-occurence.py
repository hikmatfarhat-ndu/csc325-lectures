import numpy as np

# return the index of the first occurence of element x
# if not found return -1
def bs(A,s,e,x):
    if s>=e:
        if x==A[s]:
            return s
        else:
            return -1
    m=int((s+e)/2)
    if x==A[m]:
        if x==A[m-1]:
            return bs(A,s,m-1,x)
        else:
            return m
    if x<A[m]:
        return bs(A,s,m-1,x)
    else:
        return bs(A,m+1,e,x)



input=np.random.randint(0,50,32)
#input=np.array([28,17,3,88,7,2,19,28,7,91,28,2,34,33,28,7,45,2])
x=(np.random.randint(0,50,1))[0]

y=input.copy()
y.sort()
print("{}".format(input))
print(bs(y,0,len(y)-1,x))
