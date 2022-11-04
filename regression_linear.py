#refference_section
from tabulate import tabulate
import math
import matplotlib.pyplot as plt
from sympy import *



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


print(Xint)
print(Yint)



#calculation_section
#y=a+bx

#find_b
xyup=[]
xyupdump=0
xup2=0
yup2=0
xlow1=0
xlow1dump=[]
xlow2=0





#xup2,yup2
for x in Xint:
	xup2=xup2+x

for y in Yint:
	yup2=yup2+y

#xyup
for x,y in zip(Xint,Yint):
	xyup.append(x*y)

for xy in xyup:
	xyupdump=xyupdump+xy
xyupdump=xyupdump*len(Xint)

#xlow1
for x in Xint:
	xlow1=xlow1+(x**2)
	xlow1dump.append(x**2)

xlow1=len(Xint)*xlow1

#xlow2
for x in Xint:
	xlow2=xlow2+x
xlow2=(xlow2)**2

#b_calc:
b=(xyupdump-(xup2*yup2))/(xlow1-xlow2)
print(b)

#table section
table=[]
tabledump=[]
count=0

for x,y,xy,xexp in zip (Xint,Yint,xyup,xlow1dump):
	count=count+1
	table.append(count)
	table.append(x)
	table.append(y)
	table.append(xy)
	table.append(xexp)
	tabledump.append(table)
	table=[]
print(tabledump)

header=["count","x","y","xy","x**2"]
print(tabulate(tabledump, headers=header, tablefmt="grid"),"\n")






#find a

#xmean
xmean=0
ymean=0
for x in Xint:
	xmean=xmean+x
xmean=xmean/len(Xint)
#print(xmean)

#ymean
for y in Yint:
	ymean=ymean+y
ymean=ymean/len(Yint)
#print(ymean)

a=ymean-(b*xmean)

print(a,"\n\n\n")

#find r
Dt=0
D=0

for x,y in zip(Xint,Yint):
	D=D+(y-a-(b*x))**2
for y in Yint:
	Dt=Dt+((y-ymean)**2)


r=((Dt-D)/Dt)



#equation_section
print(f"""######EQUATION SECTION######
*
*
*
*
the equation is ==> [y={a}+({b})x] 
The r Value is >>> {r}

<<<Job_Done>>>
""")




