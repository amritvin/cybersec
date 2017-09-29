kk=raw_input()
ar=kk.split(" ")
r=int(ar[0])
c=int(ar[1])
cnt =0
i=r/2
sr=""

while i>0:
    cnt+=1
    for j in range(c):
        #print "#",
        sr=sr+'#'
    #print "\n"
    sr=sr+'\n'
    for k in range(c):
        if cnt%2==0:
            if k==0:
                #print "#",
                sr=sr+'#'
            else:
                #print ".",
                sr=sr+'.'
        else:
            if k==c-1:
                #print "#",
                sr=sr+'#'

            else:
                #print ".",
                sr=sr+'.'

    #print "\n "
    sr=sr+'\n'
    i=i-1
if r%2!=0:
    for j in range(c):
        #print "#",
        sr=sr+'#'
print sr
