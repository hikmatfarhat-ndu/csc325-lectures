import queue
from numpy import *


stock_values=random.randint(1,10,5)
#stock_values=[2,3,4]
sum=0
p=queue.PriorityQueue()
for i,v in enumerate(stock_values):
    p.put((v,i))
    sum=sum+(i+1)*v

w=asscalar(random.randint(1,sum,1))
#w=15
sol=[]
ow=w
while w>0:
    x=p.get()
    # the weight=i*stock_values[i]
    if (x[1]+1)*stock_values[x[1]]<w:
      sol.append((x[1],x[1]+1))
      w=w-(x[1]+1)*stock_values[x[1]]
    else:
        
      f=int(w/stock_values[x[1]])
      if f>=1:
          sol.append((x[1],f))  
      w=0

sum=0
for (index,num) in sol:
    print("purchased {} shares at t={} for a total cost of {}\n".format(num,index+1,num*stock_values[index]))
    sum=sum+num*stock_values[index]

print("remaining balance ={}\n".format(ow-sum))
