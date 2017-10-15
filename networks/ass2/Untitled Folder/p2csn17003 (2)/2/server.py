import os, socket
import json
import sys

def game(res):
    res={"ladders": {"66": 153, "100": 129, "182": 184, "72": 154, "42": 195, "46": 62, "54": 70, "24": 148, "185": 191, "22": 86, "60": 164, "189": 190}, "die_tosses": {"1": {"1": 6, "2": 5, "3": 3, "4": 5, "5": 6, "6": 4}, "2": {"1": 4, "2": 3, "3": 6, "4": 3, "5": 2, "6": 5}, "3": {"1": 1, "2": 3, "3": 4, "4": 2, "5": 4, "6": 3}, "4": {"1": 6, "2": 1, "3": 5, "4": 2, "5": 4, "6": 2}, "5": {"1": 1, "2": 3, "3": 5, "4": 5, "5": 3, "6": 3}, "6": {"1": 5, "2": 4, "3": 5, "4": 3, "5": 4, "6": 6}, "7": {"1": 1, "2": 2, "3": 2, "4": 1, "5": 5, "6": 2}, "8": {"1": 4, "2": 3, "3": 3, "4": 2, "5": 3, "6": 5}, "9": {"1": 5, "2": 3, "3": 5, "4": 5, "5": 3, "6": 6}, "10": {"1": 6, "2": 5, "3": 1, "4": 6, "5": 2, "6": 4}, "11": {"1": 3, "2": 4, "3": 5, "4": 2, "5": 2, "6": 5}, "12": {"1": 1, "2": 6, "3": 1, "4": 6, "5": 6, "6": 1}, "13": {"1": 5, "2": 5, "3": 4, "4": 1, "5": 1, "6": 3}, "14": {"1": 4, "2": 5, "3": 2, "4": 1, "5": 6, "6": 4}, "15": {"1": 2, "2": 4, "3": 6, "4": 4, "5": 3, "6": 2}, "16": {"1": 3, "2": 1, "3": 4, "4": 2, "5": 1, "6": 2}, "17": {"1": 4, "2": 6, "3": 2, "4": 4, "5": 4, "6": 6}, "18": {"1": 5, "2": 4, "3": 2, "4": 6, "5": 6, "6": 4}, "19": {"1": 6, "2": 5, "3": 3, "4": 2, "5": 3, "6": 6}, "20": {"1": 4, "2": 4, "3": 2, "4": 1, "5": 4, "6": 3}, "21": {"1": 4, "2": 5, "3": 5, "4": 3, "5": 3, "6": 2}, "22": {"1": 5, "2": 6, "3": 2, "4": 3, "5": 2, "6": 4}, "23": {"1": 1, "2": 6, "3": 5, "4": 2, "5": 2, "6": 3}, "24": {"1": 4, "2": 5, "3": 5, "4": 2, "5": 2, "6": 6}, "25": {"1": 4, "2": 5, "3": 5, "4": 1, "5": 5, "6": 1}, "26": {"1": 2, "2": 6, "3": 3, "4": 5, "5": 5, "6": 1}, "27": {"1": 6, "2": 4, "3": 4, "4": 2, "5": 5, "6": 3}, "28": {"1": 2, "2": 1, "3": 1, "4": 6, "5": 4, "6": 5}, "29": {"1": 5, "2": 6, "3": 5, "4": 3, "5": 2, "6": 1}, "30": {"1": 4, "2": 1, "3": 6, "4": 1, "5": 1}}, "player_count": 6, "snakes": {"192": 173, "193": 112, "132": 120, "177": 147, "73": 55, "74": 18, "43": 19, "140": 136, "135": 106, "124": 41, "10": 8, "180": 142, "149": 40, "169": 161, "88": 35, "121": 34, "186": 39, "92": 81, "122": 25, "127": 123}, "board_dimension": 14}

    paths=[]
    pat=[]
    t=[]
    win=[]
    ind=0
    pcount=int(res["player_count"])
    dimension=int(res["board_dimension"])
    laddersis=res["ladders"]
    snakesis=res["snakes"]
    die=res["die_tosses"]
    windim=dimension**2

    print die

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
            if str(i) in die[str(j)]:
                li.append(die[str(j)][str(i)])
        paths.append(li)

    print paths
    d={}
    gm={}
    snlad={}
    print len(paths)
    for v in paths:
        print v
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
    return snlad



dicof={"player_count": 3,"board_dimension": 6,"ladders": {"19": 24, "27": 34, "28": 31, "32": 33},"snakes": {"6": 5, "11": 8, "30": 29, "35": 17},
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
}}

host="0.0.0.0"
port=7822
#ipaddr=sys.argv[1]
port=int(sys.argv[1])
s=socket.socket()
#host=ipaddr
s.bind((host, port))
s.listen(10)

def handle_client(s, addr, i):
    while True:
        data=s.recv(9999)
        decoded_data=data.decode("utf-8")
        strp=decoded_data.strip()
        if not strp or str(strp)== "0":
                print("\nconnection with client " + str(i) + " broken\n")
                break
        #print("  CLIENT " + str(i) + " -> " + decoded_data)
        else:
            dicof=json.loads(strp)
            msg=game(dicof)
            print msg
            m=json.dumps(msg)
            m=m+"\n"
            s.sendall(m)
            print "successfully send :\n",m


def server():
    i=1
    while i<=3:
        c, addr=s.accept()
        child_pid=os.fork()
        if child_pid==0:
                print("\nconnection successful with client " + str(i) + str(addr) + "\n")
                handle_client(c, addr, i)
        else:
                i+=1

server()
