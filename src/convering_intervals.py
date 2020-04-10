import numpy as np
def isIn(i,x):
    if x>=i and x<=i+1:
        return True
    else:
        return False


pts=np.random.uniform(1,10,10)
pts.sort()
G=[]
g=pts[0]
G.append(g)
i=1 # to simulate delete
last=g
while i< len(pts):
    if not isIn(last,pts[i]):
        g=pts[i]
        last=g
        G.append(last)
    i+=1
