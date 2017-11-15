
def readdata():
    global a,b
    with open('input.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    if len(content[0])>len(content[1]):
        a=str(content[1])
        b=str(content[0])
    else:
        b=str(content[1])
        a=str(content[0])
def lcs():
    readdata()
    global a,b
    l1=[]
    l2=[]
    lmat=[]
    temp=[]
    for i in range(len(a)):
        l1.append(a[i])
    for j in range(len(b)):
        l2.append(b[j])
    for m in range(len(b)+1):

        for n in range(len(a)+1):
                temp.append(0)
        lmat.append(temp)
        temp=[]
    for p in range(1,len(b)+1):
        for q in range(1,len(a)+1):
            if l2[p-1]==l1[q-1]:
                lmat[p][q]=(lmat[p-1][q-1])+1
            else:
                lmat[p][q]=max(lmat[p][q-1],lmat[p-1][q])

    print "THE SOLUTION IS"
    for m in range(0,len(b)+1):
        for n in range(0,len(a)+1):
                print lmat[m][n],
        print "\n"
    index = lmat[m][n]
    lcs = [""] * (index+1)
    lcs[index] = "\0"
    length= index

    i = m
    j = n
    X=b
    Y=a

    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i-=1
            j-=1
            index-=1
        elif lmat[i-1][j] > lmat[i][j-1]:
            i-=1
        else:
            j-=1
    print "length is "+str(length) +" \n" +"LCS of " + X + " and " + Y + " is " + "".join(lcs)

    with open('output.txt', 'w') as fo:
        fo.write("Length is "+str(length) +" \n"+"LCS of " + X + " and " + Y + " is " + "".join(lcs[:-1]))
lcs()
