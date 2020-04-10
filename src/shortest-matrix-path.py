# given a nxm matrix with numberical entries
# for each cell. Find the shortest path from cell (0,0)
# to cell (n-1,m-1). You are allowed to move right or down only (no left or up)
# the final cost of reaching a given cell is the sum of all costs of the cells
# on its path, including itself.

import numpy as np 

#cost=np.array([[3,6,1,4],[2,9,1,4],[5,3,9,2],[4,4,6,2]])
# cost=np.array([[7,4,8,7,9,3,7,5,0],[1,8,2,2,7,1,4,5,7],[4,6,4,7,7,4,8,2,1],[1,9,6,9,8,2,9,7,2],[5,5,7,5,8,7,9,1,4],[0,7,9,9,1,5,3,9,4]])
cost=[[7,4,8,7,9,3,7,5,0],[1,8,2,2,7,1,4,5,7],[4,6,4,7,7,4,8,2,1],[1,9,6,9,8,2,9,7,2],[5,5,7,5,8,7,9,1,4],[0,7,9,9,1,5,3,9,4]]
n=len(cost)
m=len(cost[0])
# T=np.zeros((n,m))
#Warning. Beware of the syntax below
# it just creates multiple references 
# to the same object
#T=[[0]*m]*n
T=[[0]*m for i in range(n)]
T[0][0]=cost[0][0]
for j in range(1,m):
    T[0][j]=T[0][j-1]+cost[0][j]
for i in range(1,n):
    T[i][0]=T[i-1][0]+cost[i][0]

for i in range(1,n):
    for j in range(1,m):
        T[i][j]=cost[i][j]+min(T[i][j-1],T[i-1][j])
print(T)