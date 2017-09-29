m = input()
a=0
b=1
s=0
fb=[]
fb.append(0)
fb.append(1)
for i in range(2,m):
    s=a+b
    fb.append(s)
    a=b
    b=s
print fb
