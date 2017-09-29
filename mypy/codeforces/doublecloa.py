"""s=["Sheldon", "Leonard", "Penny", "Rajesh","Howard"]
l=input()
i=5
ind=0
while (i<l):
#    print i,"::",ind

    ind=i+ind
    i=i*2
k=i/5
#print "k: ",k ,"input: ",l,"indice:",ind
ed=ind+k*5
for p in range(ind,ed+1):
    m=p+k"""
a=['Sheldon','Leonard','Penny','Rajesh','Howard']
n=input()-1
i=5;
while n>=i:
    n-=i
    i*=2
print a[n/(i/5)]
