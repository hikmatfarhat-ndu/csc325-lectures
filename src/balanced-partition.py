from numpy import *
num=10
x=random.randint(1,1000,num)

value=int(sum(x)/2)

def bottom_up(x,num,value):
    opt=zeros((num+1,value+1),dtype=bool)    
    opt[:,0]=True
    for n in range(1,num+1):
        for s in range(1,value+1):
            if s-x[n-1]>=0:
                opt[n,s]=opt[n-1,s] or opt[n-1,s-x[n-1]]
            else:
                opt[n,s]=opt[n-1,s]

    return opt


    
def get_sol(opt,x,num,value):
    done=False
    n=num
    s=value
    sol=[]
    while not (n==0 or s==0):
        if s-x[n-1]>=0 and opt[n-1,s-x[n-1]]==True:
            sol.append(x[n-1])
            s=s-x[n-1]
        n=n-1
    return array(sol)


opt=bottom_up(x,num,value)
best=(where(opt[num]==True)[0])[-1]            
sol=get_sol(opt,x,num,best)
print("x={}".format(x))
print("sol={} sum={}".format(sol,sum(sol)))
rest=setdiff1d(x,sol)
print("rest={} sum={}".format(rest,sum(rest)))
