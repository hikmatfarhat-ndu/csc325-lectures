n=3
opt=[0]*(n+1)
opt[0]=1
opt[1]=1
for i in range(2,n+1):
    opt[i]=opt[i-1]+opt[i-2]

print(opt)