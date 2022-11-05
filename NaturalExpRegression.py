#refference_section
from tabulate import tabulate
import math
#import matplotlib.pyplot as plt
#from sympy import *

print("""
>>>>>>REGULAR EXPONENTIAL REGRESSION<<<<<<
*
*
*
*
*
*
*
*
*
***********WELCOME***********
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>""")





#inp_section
Xs=input("data(x): ")
Ys=input("data(y): ")

#casting_mechanism

#array_str
Xs=Xs.split(",")
Ys=Ys.split(",")

Xint=[]
Yint=[]

#array_float
for x in Xs:
	Xint.append(float(x))
for y in Ys:
	Yint.append(float(y))


#calculation_section
#y=a*x**b

#change_var to P and Q
P=[]
Q=[]
dumper=0

for x in Xint:
	dumper=x
	Q.append(dumper)

dumper=0

for y in Yint:
	dumper=math.log(y)
	P.append(dumper)

#0.5,1.7,3.4,5.7,8.4

#find_b
pqup=[]
pqupdump=0
pup2=0
qup2=0
qlow1=0
qlow1dump=[]
qlow2=0

#xup2,yup2
for p in P:
	pup2=pup2+p

for q in Q:
	qup2=qup2+q
#print(pup2*qup2)
#xyup
for p,q in zip(P,Q):
	pqup.append(p*q)
print
for pq in pqup:
	pqupdump=pqupdump+pq
#print(pqupdump)
pqupdump=pqupdump*len(P)
#print(pqupdump)

#xlow1
for q in Q:
	qlow1=qlow1+(q**2)
	qlow1dump.append(q**2)

qlow1=len(Q)*qlow1
#print(qlow1)

#xlow2
for q in Q:
	qlow2=qlow2+q
qlow2=(qlow2)**2
#print(qlow2)
#b_calc:
b=(pqupdump-(pup2*qup2))/(qlow1-qlow2)
#print(b)

#table section
table=[]
tabledump=[]
count=0

for p,q,pq,qexp in zip (P,Q,pqup,qlow1dump):
	count=count+1
	table.append(count)
	table.append(p)
	table.append(q)
	table.append(pq)
	table.append(qexp)
	tabledump.append(table)
	table=[]
#print(tabledump)

header=["count","p","q","pq","q**2"]
print(tabulate(tabledump, headers=header, tablefmt="grid"),"\n")

#find a

#pmean
pmean=0
qmean=0
xmean=0
ymean=0
for p in P:
	pmean=pmean+p
pmean=pmean/len(P)
#print(xmean)

#qmean
for q in Q:
	qmean=qmean+q
qmean=qmean/len(Q)

#ymean
for y in Yint:
	ymean=ymean+y
ymean=ymean/len(Yint)
#print(ymean)

A=pmean-(b*qmean)
#print(A)
a=(math.e)**A
#print(a)
print("\n\n\n")

#find r
Dt=0
D=0

for x,y in zip(Xint,Yint):
	D=D+(y-(a*((math.e)**(b*x))))**2
#print(D)
for y in Yint:
	Dt=Dt+((y-ymean)**2)
#print(Dt)

r=((Dt-D)/Dt)


#equation_section
print(f"""######EQUATION SECTION######
*
*
*
*
the equation is ==> [y={a}e^{b}x] 
The r Value is >>> {r}

<<<Job_Done>>>
""")




