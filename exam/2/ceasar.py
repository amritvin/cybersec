n=input()
ec=raw_input()
m=input()
s=""
smod=25+97
cmod=25+65
nmod=9+48
doflag=0
for i in range(len(ec)):
    if ord(ec[i])>=65 and ord(ec[i])>=90:
        mod=cmod
        strt=65
        doflag=1
    if ord(ec[i])>=97 and ord(ec[i])>=122:
        mod=smod
        strt=97
        doflag=1
    if ord(ec[i])>=48 and ord(ec[i])>=57:
        mod=nmod
        strt=48
        doflag=1
    if doflag==1:
        s=s+chr((((ord(ec[i])+m)%mod)+strt)-1)
    else:
        s=s+ec[i]

print s
#122,90 48,57
