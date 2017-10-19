import heapq
from collections import defaultdict
import sys
def prims():
    orig_stdout = sys.stdout
    f = open('out.txt', 'w')
    sys.stdout = f
    g = defaultdict(list)
    weight = 0
    selected = set([])
    pq = []
    f = open ( 'input.txt' , 'r')
    l = [ map(int,line.split(' ')) for line in f ]
    n,m = l[0]
    for e in range(1,len(l)):
        a,b,w = l[e]
        g[a].append((w, b))
        g[b].append((w, a))
    start =1
    selected.add(start)
    for tup in g[start]:
        heapq.heappush(pq, tup)
    out=""

    while pq:
        w, b = heapq.heappop(pq)
        if b not in selected:
            weight += w
            selected.add(b)
            for tup in g[b]:
                heapq.heappush(pq, tup)
            for tup in g[b]:
                if tup[0]==w:
                    out=out+ str(tup[1])+"  "+str(b)+"  "+str(tup[0])
                    break
            out=out+"\n"
    print weight
    print out
    sys.stdout = orig_stdout
    f.close()
prims()
