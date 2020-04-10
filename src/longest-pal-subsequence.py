import numpy as np

X=np.array(list("XCBAACBC"))

def opt(i,j):
    if i>j:
        return 0
    if i==j:
        return 1
    if X[i]==X[j]:
        return 2+opt(i+1,j-1)
    else:
        return max(opt(i+1,j),opt(i,j-1))

r=opt(0,len(X)-1)

opta=np.zeros((len(X),len(X)))
for i in range(0,len(X)):
    opta[i,i]=1
sol=[]              
for i in range(len(X)-2,-1,-1):
     for j in range(i+1,len(X)):
         if X[i]==X[j]:
             opta[i,j]=2+opta[i+1,j-1]
         else:
             opta[i,j]=max(opta[i+1,j],opta[i,j-1])
    
nexti=0
nextj=len(X)-1
while nexti<len(X) and nextj>=nexti:
    print(nexti,nextj)
    if X[nexti]==X[nextj]:
        pos=int(len(sol)/2)
        sol.insert(pos,X[nexti])

        if not nextj==nexti:
            sol.insert(pos+1,X[nexti])            
        nexti=nexti+1
        nextj=nextj-1
    elif opta[nexti,nextj]==opta[nexti+1,nextj]:
        nexti=nexti+1
    else:
        nextj=nextj-1


    
