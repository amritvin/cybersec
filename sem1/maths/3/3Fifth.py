tw=[]
th=[]
print "ENTER THE ELEMENTS FOR 2x2 matrix:\n "
for i in range(2):
    tw1=map(int,raw_input().split(" "))
    tw.append(tw1)

m1=tw[0][0]*tw[1][1]
m2=tw[1][0]*tw[0][1]
det1=m1-m2
print "ENTER THE ELEMENTS FOR 3x3 matrix:\n "
for i in range(3):
    tw3=map(int,raw_input().split(" "))
    th.append(tw3)
n1=th[0][0]*((th[1][1]*th[2][2])-th[2][1]*th[1][2])
n2=th[0][1]*((th[1][0]*th[2][2])-th[2][0]*th[1][2])
n3=th[0][2]*((th[1][0]*th[2][1])-th[2][0]*th[1][1])
det2=n1-n2+n3
print "det of 2x2 is :",det1,"det of 3x3 is :",det2
tw[0][1]=-1 *tw[0][1]
tw[1][0]=-1 *tw[1][0]
inv=[]
if det1==0:
    print "no INVERSE"
else:
    for i in tw:
            for j in i:
                inv.append(float(j)/det1)
    print "inverse is : ",inv
