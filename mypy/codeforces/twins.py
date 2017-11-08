"""c=input()
s=raw_input()
k=s.split(" ")
for e in k:
	e=int(e)
k.sort()
su=0
cnt=0
mx=max(k)
for e in k:
	su=su+int(e)
	if su>max:
		cnt+=1
print su,cnt"""
x=int(raw_input())
c=0
a=map(int,raw_input().split())
y=sorted(a,reverse=True)
for i in range(1,len(y)+1):
    if sum(y[:i])>sum(y[i:]):
        c+=1
        break
    else:
        c+=1

print c
