s=raw_input()
ab=set(s)
sr="hello"
abc=set(sr)
if ab-abc:
	print"YES"
else:
	if(abc==ab):
		print"NO"
	else:
		print"YES"
	
