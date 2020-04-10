f=open("sched3.smt","w")

# we need the following variables
# s[i] i=1..8 starting time of job i
# e[i] i=1..8 ending time of job i
# p[i] i=1..8 worker who accomplishes job i
# job length l[i]
#l=[4,5,6,7,8,9,10,11]
l=[4,5,6,7,8,9]
for i in range(1,len(l)+1):
    f.write("(declare-const p{} Int)\n".format(i))
    f.write("(declare-const s{} Int)\n".format(i))
    f.write("(declare-const e{} Int)\n".format(i))
    f.write("(assert (and (>= p{} 1) (<= p{} 3)))\n".format(i,i))
#add the constraint that e[i]-s[i]=l[i]
for i in range(1,len(l)+1):
    f.write("(assert (= e{} (+ s{} {})))\n".format(i,i,l[i-1]))

# The variable T will be minimize. It is the time when
# all jobs finish
f.write("(declare-const T Int)\n")
#make sure that every worker does one job at a time
for i in range(1,len(l)+1):
    for j in range(i+1,len(l)+1):
        f.write("(assert (=> (= p{} p{}) (or (>= s{} e{}) (>= s{} e{}))))\n".format(i,j,i,j,j,i))
# a job can start at 0 and must at or before T
for i in range(1,len(l)+1):
    f.write("(assert (and (>= s{} 0)(<= e{} T)))\n".format(i,i))
# job 2 cannot start until job 6 and 7 finish
#f.write("(assert (>= s2 e6))\n")
#f.write("(assert (>= s2 e7))\n")
# job 3 cannot start until jobs 2 and 6 finish
f.write("(assert (and (>= s3 e2) (>= s3 e6)))\n")
# jobs 1 and 4 must be performed by worker 2
f.write("(assert (= p1 2))\n")
f.write("(assert (= p4 2))\n")

f.write("(minimize T)\n")
for i in range(6):
    f.write("(minimize s{})\n".format(i))
f.write("(check-sat)\n")
f.write("(get-model)\n")