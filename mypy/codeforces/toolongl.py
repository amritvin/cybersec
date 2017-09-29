a=raw_input()
m=int(a)
ss=""
s=[]
for i in range(m):
	t=raw_input()
	s.append(t)
	l=len(s[i])
	if(l>10):
		ss=ss+"#"+s[i][0]+str(l-2)+s[i][l-1]
	else :
		ss=ss+"#"+s[i]
	
d= ss.split("#")
for i in d:
	print i
