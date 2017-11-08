n=input()
se=[]
price=[]
meat=[]
for i in range(n):
    se.append(raw_input().split(" "))
for e in se:
     price.append(int(e[1]))
     meat.append(int(e[0]))
f=min(price)
i=0
for ele in price:
    if ele==f:
        break;
    i=i+1
s=0
p=0
if n!=1:
    for k in range(i):
        s=s+meat[k]*price[k]
    for j in range(k+1,len(meat)):
        p=p+meat[j]*price[i]
    print s+p
else:
    print f*meat[0]
