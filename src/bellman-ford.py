import numpy as np
num=6
opt=np.full((num,num),100)
opt[0,0]=0
edge=np.full((num,num),100)

f=open("graph1.txt","r")
input=f.read()
lines=input.splitlines()
for line in lines:
  x=line.split(":")
  cost=x[1]
  y=x[0].split("-")
  s=y[0]
  d=y[1]
  edge[int(s),int(d)]=int(cost)

# for l in range(1,num): #iterate over length
#      for n in range(0,num): #iterate over the nodes
#          opt[n,l]=min(opt[n,l-1],min(opt[:,l-1]+edge[:,n]))
pred=np.full(num,-1)
for l in range(1,num): #iterate over length
  for n in range(0,num): #iterate over nodes
    opt[n,l]=opt[n,l-1]
    for m in range(0,num):#iterate over neighborsxs
      s=opt[m,l-1]+edge[m,n]
      if s<opt[n,l]:
        opt[n,l]=s
        pred[n]=m
      

# for n in range(0,num):
#   for k in range(1,num):
#     if opt[k,5]==opt[n,4]+edge[n,k]:
#       pred[k]=n


for n in range(0,num):
  print("&".join(list(map(str,opt[n]))))
