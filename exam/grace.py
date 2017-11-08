m=raw_input()
a,b=m.split(" ")
a=int(a)
b=int(b)
#b=int(m[2])
lis=[]
scr=raw_input()
lis=scr.split(" ")
count=0
f=0
for i in range(0,a):
    if int(lis[i])<=0:
        f+=1
    if int(lis[i])>=int(lis[b-1]):
        count+=1
if f==a:
    print 0
else:
    print count
