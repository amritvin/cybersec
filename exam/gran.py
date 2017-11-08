s=raw_input()
k,n,w=s.split(" ")
su=0
for i in range(1,int(w)+1):
    su=su+int(k)*i
if su>int(n):
    print su-int(n)
else:
    print 0
