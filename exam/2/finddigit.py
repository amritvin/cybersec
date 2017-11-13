n=input()
k=[]
cont=0
for i in  range(n):
    k.append(input())
for e in k:
    s=e
    while(s):
        r=s%10
        s=s/10
        if(r!=0):
            if e%r==0:
                cont=cont+1
    print cont
    cont=0
