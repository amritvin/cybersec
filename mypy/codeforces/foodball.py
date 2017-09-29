s=input()
i=0
for i in range(len(s)) :
	if s[i+1]==s[i] :
		cn+=1
		print cn,
	else:
		cnt=0
	if cnt==7  :
		fl=1
		break;
if fl==1:
	print "YES"
else : 
	print "NO"
		

		
