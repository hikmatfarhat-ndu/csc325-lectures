import itertools

vars=[1,2,3,4]

for (i,j) in itertools.combinations(vars,2):
   print(i,j)
for (i,j,k) in itertools.combinations(vars,3):
   print(i,j,k)
