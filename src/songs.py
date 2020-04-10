import numpy as np

m=60
i,j,w,n=0,0,m,20

cd=[]
cd.append([])
l=np.random.randint(1,int(m/2),n)
#l=[12,28,17,34,13,18,19,25,19,24]
while i<n:
    if l[i] <w:
        w=w-l[i]
        i=i+1
        cd[j].append(i)
    else:
        j=j+1
        cd.append([])
        w=m
