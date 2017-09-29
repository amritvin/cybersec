m=raw_input()
ar=m.split()
g=int(ar[0])
s=0
p=[]
for i in range(len(ar)-1):
    s=s+int(ar[i+1])
    if s==g:
        p.append(ar[i+1])
    s=int(ar[i+1])
if len(p)>1:
    print p[1]
else:
    print p[0]
