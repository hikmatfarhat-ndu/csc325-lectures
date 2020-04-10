from collections import Counter
f=open("hauffman.py","r")
str=f.read()
#remove newline characters using splitlines
#rejoin the strings together
str="".join(str.splitlines())
counts=Counter(str)
total=0
freq=[]
for k,v in counts.items():
    total+=v

for k,v in counts.items():
    freq.append((v/total,k))
