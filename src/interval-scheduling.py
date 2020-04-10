import queue
import  numpy as np 
def overlap(x,y):
    if x[1]>y[0]:
        return True
    else:
        return False

i=(1,7)
j=(4,9)
print(overlap(i,j))
start=np.random.randint(1,50,5)
intervals=[]
p=queue.PriorityQueue
for idx,s in enumerate(start):
    e=np.asscalar(np.random.randint(1,6,1))
    intervals.append((s,s+e))
    p.put((s+e,idx))
print(intervals)