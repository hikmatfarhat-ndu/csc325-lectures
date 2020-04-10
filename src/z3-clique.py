
# Finds the maximum clique set
import itertools
import z3 
import networkx as nx

n=None
file_name=None
input_file=None
source=None
while True:
   source=input("Input graph random or from a file?(R/F)")
   if source!="R" and source!="F" :
      print("Please answer R or F\n")
      continue
   elif source=="R":
      n=int(input("How many nodes? "))
      break
   else:
      file_name=input("file name path?\n")
      break


if n!=None:
# Uses networkx to genrate
# a radom erdos graph 
   G=nx.erdos_renyi_graph(n,0.6)
   edges=G.edges
# TODO 1 can we use networkx to find the maximal clique
#   nx_max=nx.maximal_independent_set(G)
#  l=len(nx_max)
#   print(nx_max)
elif file_name!=None:   
   input_file=open(file_name,"r")
   l=input_file.readline()
   n,k=list(map(int,l.split()))
   rest=input_file.read()
   lines=rest.splitlines()
   edges=[tuple(map(int,line.split())) for line in lines]
else :
   print("something wrong happened")
   exit()


#create space for n variables 
vars=[None]*n

#create n z3 Boolean variables
for i in range(0,n):
   vars[i]= z3.Bool("x"+str(i))

# TODO 2: see TODO 1
#if source=="R":
#   print("networkx found IS of size {} looking for larger".format(l))

#all graphs have clique of size 2
# unless there are no edges
k=2

last_model  = None

# list of NOT connected nodes
notconnected=[]
for i in range(0,n):
   for j in range(i+1,n):
      if (i,j) not in edges:
         notconnected.append((i,j))

# Each iteration increase the size
# by one to see if there are bigger IS

while True:
   solver=z3.Solver()
# we need all combinations of n-k+1 variables
   comb=n-k+1
#create an Or clause for each combination of n-k+1 variables
   for c in itertools.combinations(vars,comb):
      solver.add(z3.Or(c))
# Add constraints on the edges   
   for (s,e) in notconnected:
      solver.add(z3.Or(z3.Not(vars[s]),z3.Not(vars[e])))

   r = solver.check()
   if r != z3.sat:
      k=k-1
      break
   last_model=solver.model()
   if source=="R":
      k = k + 1
   else:
      break
   

if last_model != None:
   print("Found clique of size {}".format(k))
   f=open("erdos.txt","w")
   f.write("graph G {\n graph [nodesep=\"0.3\"];\n")
# TODO 3: if we include networkx result
# compare with z3-independent.py  

   f.write("{ node [color=red] ")
   result=last_model.decls();
   for d in result:
      if(last_model[d]==True):
         f.write("{} ".format(d.name()))
   f.write("}\n")
   for u,v in edges:
      if last_model[vars[u]]==True and last_model[vars[v]]==True:
         f.write("x{} -- x{}[color=red];\n".format(u,v))  
      else:    
         f.write("x{} -- x{};\n".format(u,v))
   f.write("}")
else:
   print("No clique of size {} exits".format(k))
