
# Finds the maximum independent set
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
# a radom erdos graph and computes "maximal" IS using
# networkx. 
   G=nx.erdos_renyi_graph(n,0.3)
   edges=G.edges
   nx_max=nx.maximal_independent_set(G)
   l=len(nx_max)
   print(nx_max)
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


if source=="R":
   print("networkx found IS of size {} looking for larger".format(l))
   k=l

last_model  = None

# start look for IS of the same size as returned 
# by networkx. Each iteration increase the size
# by one to see if there are bigger IS
while True:
   solver=z3.Solver()
# we need all combinations of n-k+1 variables
   comb=n-k+1
#create an Or clause for each combination of n-k+1 variables
   for c in itertools.combinations(vars,comb):
      solver.add(z3.Or(c))
# Add constraints on the edges   
   for (s,e) in edges:
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
   print("Found an IS of size {}".format(k))
   f=open("erdos.txt","w")
   f.write("graph G {\n graph [nodesep=\"2\"];\n")
   if source=="R":
      f.write("subgraph networkx{\nlabel=\"networkx\";\n ")
      f.write("{node [color=blue,] ")
      for y in nx_max:
         f.write("y{} ".format(y))
      f.write("}\n")
      for u,v in edges:
         f.write("y{} -- y{};\n".format(u,v))

   f.write("}\n subgraph z3 {\n label=\"z3\";\n")
   f.write("{ node [color=red] ")
   for d in last_model.decls():
      if(last_model[d]==True):
         f.write("{} ".format(d.name()))
   f.write("}\n")
   for u,v in edges:
      f.write("x{} -- x{};\n".format(u,v))
   f.write("}}")
else:
   print("No IS of size {} exits".format(k))
