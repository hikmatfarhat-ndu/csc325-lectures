

def nqueen(Q,r):
  if r==n:
     print(Q)
  else:
     for j in range(n):
        legal=True
        for i in range(r):
           if (Q[i]==j) or (Q[i]==j+r-i) or (Q[i]==j-r+i):
             legal=False
        if legal:
          Q[r]=j
          nqueen(Q,r+1)

n=4    
Q=[0]*n
nqueen(Q,0)
