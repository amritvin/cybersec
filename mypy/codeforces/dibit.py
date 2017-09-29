m=raw_input()
n=raw_input()
s=""
for a in range(0,len(m)):
    if m[a]==n[a]:
            s=s+'0'
    else:
        s=s+'1'
print s
