s=input()
m=raw_input()
k=m.count('A')
l=m.count('D')
if k>l:
    print "Anton"
if l>k:
    print "Danik"
if k==l:
    print "Friendship"
