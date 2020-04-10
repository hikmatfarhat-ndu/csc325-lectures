import itertools
with open("independent.txt","r") as f:
   n=int(f.readline())
   input=f.read()
   lines=input.splitlines()

edges=[]
for line in lines:
  s,e=line.split()
  edges.append((int(s),int(e)))
vars=range(1,n+1)
k=4
comb=n-k+1
clauses=[]

for c in itertools.combinations(vars,comb):
   clauses.append(c)
for (s,e) in edges:
   clauses.append((-s,-e))

out=open("is.cnf","w")
out.write("p cnf {} {}\n".format(n,len(clauses)))
for c in clauses:
    out.write(" ".join(map(str,c))+" 0\n")
