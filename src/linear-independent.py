import numpy as np 

#create random linear independent
#set instances with their solutions

#generate n random values
#to be used as values for the consecutive nodes
n=16
V=np.random.randint(1,20,n)
V=np.array( [6,7,6,15,3,9,16,10,18,1,10,18,1,9,6,11] )
# V=np.array([6,7,6,15,3,9,16,10,18,1,10,18,1,9,6,11])
opt=np.zeros((n+1))
for i in range(1,n+1):
    opt[i]=max(opt[i-1],V[i-1]+opt[i-2])
print("[",end="")
for i,v in enumerate(V):
    if i!=len(V)-1:
        print("{},".format(v),end="")
    else:
        print("{}".format(v),end="")
print("]")    
print("answer={}".format(opt[n]))
print("wrong answer 1={}".format(opt[n-1]))
print("wrong answer 2={}".format(opt[n-2]))
print("wrong answer 3={}".format(opt[n-3]))
print("wrong answer 4={}".format(opt[n-4]))
f=open("independent.tex","w")
f.write("\\documentclass{article}\n")
f.write("\\usepackage{tikz}\n")
f.write("\\begin{document}\n")
f.write("\\begin{tikzpicture}\n")
for i in  range(0,len(V)):
    j=i+1
    f.write("\\node[draw,circle] at ({},{}){{$X_{}$}};\n".format(2*j,0,j))
    f.write("\\node at ({},1) {{${}$}};\n".format(2*j,V[i]))
    if j!=len(V):
        f.write("\\draw ({},0)--({},0);\n".format(2*j+0.5,2*j+2-0.5))
f.write("\\end{tikzpicture}\n")
f.write("\\end{document}\n")
f.close()