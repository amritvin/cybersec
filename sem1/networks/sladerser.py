import socket
import sys
import json
def game(res):

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
    return snlad

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 8753)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections

dictd={}
sock.listen(3)
print('waiting for a connection')
connection, client_address = sock.accept()
data=connection.recv(2024)
data=data.strip()
data=json.loads(data)
while data!="0\n":
    #while True:
    #print "CLIENT :  "
    #print('received {!r}'.format(data))
    dictd=data
    print dictd
    print('Recieving . . .')
    r=game(dictd)
    s=json.dumps(r)
    connection.sendall(s)
    data=connection.recv(2024)
    data=data.strip()
    data=json.loads(data)

connection.close()
#{"player_count": 3,"board_dimension": 6,"snakes": {"33": 18, "27": 6, "28": 12, "15": 13},"ladders": {"34": 35, "5": 17, "22": 25, "23": 29},"die_tosses": {     "1": {"1": 4, "2": 4, "3": 4},     "2": {"1": 6, "2": 5, "3": 4},     "3": {"1": 4, "2": 6, "3": 4},     "4": {"1": 5, "2": 5, "3": 2},     "5": {"1": 6, "2": 5, "3": 5},     "6": {"1": 6, "2": 4, "3": 3},     "7": {"1": 4, "2": 2, "3": 6},     "8": {"1": 5, "2": 4, "3": 1},     "9": {"1": 5, "2": 3, "3": 5},     "10": {"1": 5, "2": 1,"3": 3}}}
