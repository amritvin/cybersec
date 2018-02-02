s="3||2||1||1:2,0,S,W||3:0,1,S||0||2||2:F,6||3:4,5,W,3,0||0||"
#def uno(s):
score={'S':20,'T':20,'R':20,'W':50,'F':50,'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,',':0}
l=s.split("||")
siz=len(l)
it=0

ridd=0
print "size : ",siz
print "list is : ", l

np=int(l[0])
nr=int(l[1])
rid=[l[2]]
play= []
p=[]
lofp=range(1,int(np)+1)
def crk(fulllist):

	play=fulllist
	ro_score=[]
	sum1=0
	pinl=[]

	for s in play:
		ro_score.append(s.split(":"))
	print"her:::::::", ro_score
												#cracking round 1
	for n in  range(0,len(ro_score)):
		pinl.append(int(ro_score[n][0][0]))
	#print pinl, lofp	#print ro_score[1][0][0]
	for k in ro_score[0][1]:
		sum1+=score[k]
	for k in ro_score[1][1]:
		sum1+=score[k]
		#x+=1
		#print s
	pwin=[]
	pwin=list(set(lofp)-set(pinl))
	return str(pwin[0]) +":"+str(sum1)
def splt(n,siz,l):
	#global z
	ridd=[]
	play=[]
	for i in range(n,siz):
		if l[i]=="0":
			break
		else:
			play.append(l[i])
	global rid2,it
	if(i<siz):
		ridd.append(l[i+1])
	it=i
	#rid2=rid[0]
	print it
	#return play
#	global s
	j=""
	#t=""
	print "her :",play
	j=crk(play)
	#t=crk(p)
	s=j.split(":")
	#s1=t.split(":")
	#print j,t,s[0],s[1],s1[0],s1[1]
	#if int(s[1])>int(s1[1]):
	#	print s[0],"is winner with score: ",s[1]
	a=s[1]
	return a
	#else:
		#print s1[0],"is winner with score",s1[1]

#for j in range(1,int(np)+1):
	#lofp.append(j)

print "no. of rounds :", nr
print "no. of players :", np
p=3
play1=[]
while p<siz:
	play1.append(splt(p,siz,l))
	p+=np+1
	rid.append(l[p-1])
print rid
print play1

#p=splt(it+2,siz,l)

"""	if l[n]=="0":
		break
	else:
		p.append(l[n])
"""

print "list: " ,play1 ," P: " ,p

"""if (x=roundwin(play1))>(y=roundwin(p)):
	print s[0],"is winner"
else:

"""





































"""#cracking round 2
ro_score1=[]
for s in p:
	ro_score1.append(s.split(":"))
sum2=0
print ro_score1
#cracking round 1
pinl1=[]
#m=0
for n in  range(0,len(ro_score1)):
	pinl1.append(int(ro_score1[n][0][0]))
print pinl1, lofp
#print ro_score[1][0][0]

for k in ro_score1[0][1] :
	sum2+=score[k]

#m+=1

for k in ro_score[1][1] :
	sum2+=score[k]
	s=sum2
	#x+=1
#print s
pwin1=[]
pwin1=list(set(lofp)-set(pinl1))
print pwin1,": ",sum2
if sum1>sum2:
	print "winner :" ,pwin1 ,"score= ",sum1+sum2
"""
