"""res={"player_count": 3,"board_dimension": 6,"ladders": {"19": 24, "27": 34, "28": 31, "32": 33},"snakes": {"6": 5, "11": 8, "30": 29, "35": 17},
"die_tosses": {
"1": {"1": 5, "2": 1, "3": 5},
"2": {"1": 5, "2": 1, "3": 6},
"3": {"1": 5, "2": 3, "3": 3},
"4": {"1": 4, "2": 1, "3": 5},
"5": {"1": 1, "2": 3, "3": 3},
"6": {"1": 6, "2": 6, "3": 6},
"7": {"1": 3, "2": 6, "3": 3},
"8": {"1": 5, "2": 3, "3": 4},
"9": {"1": 1, "2": 4, "3": 3},
"10": {"1": 1, "2": 2, "3": 3}
}}"""
res= {"player_count": 3,
 "board_dimension": 6,
"snakes": {"33": 18, "27": 6, "28": 12, "15": 13},
"ladders": {"34": 35, "5": 17, "22": 25, "23": 29},
"die_tosses": {
     "1": {"1": 4, "2": 4, "3": 4},
     "2": {"1": 6, "2": 5, "3": 4},
     "3": {"1": 4, "2": 6, "3": 4},
     "4": {"1": 5, "2": 5, "3": 2},
     "5": {"1": 6, "2": 5, "3": 5},
     "6": {"1": 6, "2": 4, "3": 3},
     "7": {"1": 4, "2": 2, "3": 6},
     "8": {"1": 5, "2": 4, "3": 1},
     "9": {"1": 5, "2": 3, "3": 5},
     "10": {"1": 5, "2": 1, "3": 3}
}}



paths=[]
pat=[]
t=[]
win=[]
ind=0
pcount=res["player_count"]
dimension=res["board_dimension"]
laddersis=res["ladders"]
snakesis=res["snakes"]
die=res["die_tosses"]
windim=dimension**2
def slcal(p,k):
    su=0
    tem=[]
    dic={}

    for e in p:
        if su+e<=windim:
            su=su+e
            tem.append(su)
            if str(su) in snakesis:
                    su=(int(snakesis[str(su)]))
                    tem.append(su)
            if str(su) in laddersis:
                 su=(int(laddersis[str(su)]))
                 tem.append(su)
            if su==windim:
                win.append(k)
    dic[str(k)]=su
    pat.append(tem)
    return dic



i=1
j=1
final_positions={}
squares_traversed={}
trav={}
for i in range(1,pcount+1):
    li=[]
    for j in range(1,len(die)+1):
        li.append(die[str(j)][str(i)])
    paths.append(li)

#print paths
d={}
gm={}
snlad={}
for v in paths:
    final_positions.update(slcal(v,ind+1))
    trav[str(ind+1)]=pat[ind]
    squares_traversed.update(trav)
    ind=ind+1
if len(win)==0:
    d["winner"]=None
    gm["game_state"]="progress"
else:
    d["winner"]=win[0]
    gm["game_state"]="finished"

snlad["game_state"]=gm["game_state"]
snlad["winner"]=d["winner"]
snlad["final_positions"]=final_positions
snlad["squares_traversed"]=squares_traversed
print snlad
