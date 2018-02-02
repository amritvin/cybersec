m=input("enter a number: ")
n=m
pfact=[]
while m!=1:
    for i in range(2,m+1):
        if(m%i==0):
            break
    m=m/i
    pfact.append(i)
if pfact[0]==n:
    pfact.insert(0,1)
print "prime factors are: ",pfact
