s=raw_input()
c=1
fl=0
for i in range(1,len(s)) :
	if ( s[i]==s[i-1] ):
		c+=1
	
	else :
		c=1
	
	if c==7:
		fl=1
		break;
if fl==1:
	print "YES"
else:
	print"NO"
