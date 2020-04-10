from numpy import *
num=10
x=random.randint(1,40,num)
#x=array([12,8,6,13,7])
value=asscalar(random.randint(50,100,1))



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

def subset_sum(A,n,s):
    if s==0:
        return True
    if n==0:
        return False
    if s-A[n-1]>=0:
        return subset_sum(A,n-1,s) or subset_sum(A,n-1,s-A[n-1])
    else:
        return subset_sum(A,n-1,s)
    
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

r=subset_sum(x,num,value)
opt=bottom_up(x,num,value)
solution=None
if opt[num,value]==True:
    solution=get_sol(opt,x,num,value)
            
            
