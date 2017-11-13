n=input()
s=""
for i in range(n):
    for spc in range(n,i+1,-1):
        s=s+" "
    for j in range(i+1):
        s=s+"#"
    s=s+"\n"
print s
