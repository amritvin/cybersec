#!/bin/python

import sys

def gameOfThrones(s):
    s=s.lower()
    l=len(s)
    lis=[]
    count=[]
    f=0
    for i in range(l):
        lis.append(s[i])
    se=set(lis)
    if len(se)!=l:
        for e in se:
            count.append(lis.count(e))
        for ele in count:
            if ele%2==0:
                f=f+1
        if f>0:
            res="YES"
    else:
        res="NO"
    return res

s = raw_input().strip()
result = gameOfThrones(s)
print(result)
