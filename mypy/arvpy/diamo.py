n=5
s=""
for i in range(0,n+1):
    for j in range(i):
        s=s+"+"
    s=s+"\n"
for i in range(n+1,0,-1):
    for j in range(i):
        s=s+"+"
    s=s+"\n"
print s
