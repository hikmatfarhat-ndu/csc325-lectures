#not working correctly 
#will come back to this problem later
import random
def median(A,B,sa,ea,sb,eb):
    ma=int((sa+ea)/2)
    mb=int((sb+eb)/2)
    if (sa==ea) or (sb==eb):
        if A[ma]>B[mb]:
            return A[ma]
        else:
            return B[mb]
    if A[ma]<B[mb]:
        return median(A,B,ma,ea,sb,mb)
    else:
        return median(A,B,sa,ma,mb,eb)

#iterative version
def medianI(A,B,sa,ea,sb,eb):
    even=((len(A)+len(B))/2)%2==0   
    while (sa!=ea) and (sb!=eb):
        ma=int((sa+ea)/2)
        mb=int((sb+eb)/2)
    
        if A[ma]<B[mb]:
            sa=ma
            eb=mb
        else:
            ea=ma
            sb=mb
    if even:
        print("even")
        return (A[ma]+B[mb])/2
    if A[ma]>B[mb]:
        return A[ma]
    else:
        return B[mb]
#A=[random.randint(1,100) for i in range(0,5)]
#B=[random.randint(1,100) for i in range(0,6)]
A=[1,2]
B=[3,4]
A.sort()
B.sort()
print("A={}".format(A))
print("B={}".format(B))
print(median(A,B,0,len(A)-1,0,len(B)-1))
print(medianI(A,B,0,len(A)-1,0,len(B)-1))