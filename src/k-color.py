import itertools
import os

f=open("independent.txt","r")
n=int((f.readline()).split()[0])
rest=f.read()
lines=rest.splitlines()
edges=[tuple(map(int,line.split())) for line in lines]

clauses=[]
colors=range(1,4)
color_names=None
if len(colors)==3:
  color_names=["Red","Green","Blue"]
def varnum(i,j):
    assert(i in range(1,n+1) and j in colors)
    return len(colors)*i-j+1

def exactly_one_of(literals):
    clauses.append([l for l in literals])
    for pair in itertools.combinations(literals,2):
        clauses.append([-l for l in pair])

#constraints for each node
for node in range(1,n+1):
    exactly_one_of([varnum(node,color) for color in colors])
for u,v in edges:
    for c in colors:
     clauses.append([-varnum(u,c),-varnum(v,c)])



with open ("tmp.cnf","w") as f:
     f.write("p cnf {} {}\n".format(3*n,len(clauses)))
     for c in clauses:
         c.append(0)
         f.write(" ".join(map(str,c))+"\n")
os.system("minisat tmp.cnf tmp.sat")
with open("tmp.sat","r") as satfile:
     for line in satfile:
         if line.split()[0]=="UNSAT":
             print("there is no solution\n")
         elif line.split()[0]=="SAT":
             pass
         else:
             assignment=[int(x) for x in line.split()]
             for a in assignment:
                 if a>0:
                     r=a%len(colors)
                     d=int((a-1)/len(colors))
                     if color_names==None:
                       print("node {} assigned color {}\n".format(d+1,r))
                     else:
                       print("node {} assigned color {}\n".format(d+1,color_names[r]))

                        
                 

