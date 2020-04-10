import itertools
import os
import z3

f=open("graph1.txt","r")
n=int((f.readline()).split()[0])
rest=f.read()
lines=rest.splitlines()
edges=[tuple(map(int,line.split())) for line in lines]


colors=range(0,3)
color_names=["Blue","Green","Red"]
#number of nodes times the number of colors
nvars=n*len(colors)
vars=[None]*nvars

solver=z3.Solver()


def varnum(i,j):
    assert(i in range(0,n) and j in colors)
    return len(colors)*i+j

# define variables
for i in range(0,n):
    for j in colors:
        vars[varnum(i,j)]=z3.Bool("x"+str(varnum(i,j)))


def exactly_one_of(literals):
   
    solver.add(z3.Or([vars[l] for l in literals]))
   
    for a,b in itertools.combinations(literals,2):
        solver.add(z3.Or(z3.Not(vars[a]),z3.Not(vars[b])))

#constraints for each node
for node in range(0,n):
    exactly_one_of([varnum(node,color) for color in colors])

for u,v in edges:
  for c in colors:
      x=varnum(u,c)
      y=varnum(v,c)
      solver.add(z3.Or(z3.Not(vars[x]),z3.Not(vars[y])))

if(solver.check()==z3.sat):
    print("satout")
    m=solver.model()
    for d in m.decls():
        if(m[d]==True):
            head=(d.name()).rstrip("0123456789")
            num=int((d.name())[len(head):])
            q=int(num/3)
            r=num%3
            print("node {} has color {}".format(q,color_names[r]))

