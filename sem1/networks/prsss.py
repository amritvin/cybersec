import json
s=raw_input("E:")
#s="3||2||1||1:2,0,S,W||3:0,1,S||0||2||2:F,6||3:4,5,W,3,0||0||"
score={'S':20,'T':20,'R':20,'W':50,'F':50,'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,',':0}
l=s.split("||")
siz=len(l)
np=int(l[0])
nr=int(l[1])
rid=[l[2]]
play= []
p=[]
lofp=range(1,int(np)+1)

def crk(fulllist):
        pinl=[]
        ro_score=[]
        sum1=0;
        for s in fulllist:
            r,q=s.split(":")
            ro_score.append(q)
            pinl.append(int(r))
        print ro_score
        print len(pinl)
	#cracking round #
    #for n in range(0,len(ro_score)):
	 #   pinl.append(int(ro_score[n][0][0]))
        print pinl, lofp

        for i in range(0,len(pinl)):
            #print ro_score[1][0][0]
    	       for k in ro_score[i]:
                   sum1+=score[k]
    		#x+=1
    		#print s
    	pwin=[]
    	pwin=list(set(lofp)-set(pinl))
    	return str(pwin[0]) +":"+str(sum1)
def splt(n,siz,l):
        play=[]
    	for i in range(n,siz):
    		if l[i]=="0":
    			break
    		else:
    			play.append(l[i])
        return play



#print crk(['1:2,0,S,W','3:0,1,S'])
p=3
play1=[]
rwin={}
while p<siz:
    w=crk(splt(p,siz,l))
    x=w.split(":")
    y = map(int, x)
    play1.append(y)
    p+=np+1
    rid.append(l[p-1])
print play1
r=1
for s in play1:
        rwin[r]=s[0]
        r+=1
print rwin
for i in range(0,len(play1)):
    for j in range(0,len(play1)):
        if(play1[i][1]>play1[j][1]):
            s=play1[i]
            play1[i]=play1[j]
            play1[j]=s
winner=play1[0][0]
scores={}
u=1
e=0
for n in range(0,np):
    if e<len(play1):
        scores[u]=play1[e][1]
        u+=1
        e+=1
    else:
        scores[u]=0
        u+=1

print winner
print scores

d={}
d["round_winners"]=rwin
d["overall_winner"]=winner
d["scores"]=scores
r = json.dumps(d)
print r
