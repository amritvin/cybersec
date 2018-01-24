import os
import sys
import socket
import json
import signal

signal.alarm(50)
def run(conn):
    print "Starting the Thread"
    while True:
        print "Repeting the Thread"

        game = {
            "player_count": 3,
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
            }
        }

        Winner = 0

        recv = conn.recv(999999)

        #print self.getName(), "Recieved-->", recv

        if recv.strip() == "0":
            print recv.strip()
            print "Client Exiting"
            break
        print "===>", repr(recv), type(recv.strip())
        game = json.loads(recv)
        # print game,type(game)

        Rounds = []
        # print game["die_tosses"].keys()

        for k in game["die_tosses"].keys():
            Rounds.append(k)

        Rounds = map(int, Rounds)
        Rounds = sorted(Rounds)
        Player_Score = {}
        for m in range(1, game["player_count"] + 1):
            Player_Score[m] = []
        for i in Rounds:
            pass
            # print game["die_tosses"][str(i)]
            for j in range(1, game["player_count"] + 1):
                # print game["die_tosses"][str(i)][str(j)]
                if len(Player_Score[j]) == 0:
                    Current_Score = 0
                else:
                    Current_Score = Player_Score[j][-1]
                # print game["die_tosses"][str(i)]
                if str(j) not in game["die_tosses"][str(i)].keys():
                    # print "j not there"
                    continue
                # print Player_Score[j]
                # print j, "==>", Current_Score, game["die_tosses"][str(i)][str(j)]
                # print "===========",i,j, game["die_tosses"]
                # print "++++++++++++++",game["die_tosses"][str(i)][str(j)]
                Current_next = Current_Score + game["die_tosses"][str(i)][str(j)]
                # print Player_Score[j]
                if Current_next <= game["board_dimension"] ** 2:
                    Player_Score[j].append(Current_next)
                if Current_next == game["board_dimension"] ** 2 and Winner == 0:
                    Winner = j
                Current_Score1 = Player_Score[j][-1]
                if str(Current_Score1) in game["ladders"].keys():

                    ladder_end = game["ladders"][str(Current_Score1)]
                    Player_Score[j].append(ladder_end)
                    if Current_Score1 == game["board_dimension"] ** 2:
                        if Winner == 0:
                            # Winner = j
                            pass

                if str(Current_Score1) in game["snakes"].keys():
                    # print "sdjfsdkjfoiwjrjsdfksdkfj"
                    snake_tail = game["snakes"][str(Current_Score1)]
                    Player_Score[j].append(snake_tail)

        # print Winner

        # print Player_Score
        if Winner == 0:
            Win_Stat = None
        else:
            Win_Stat = Winner

        # print Win_Stat
        f_positions = {}
        for m in Player_Score.keys():
            f_positions[str(m)] = Player_Score[m][-1]

        # print f_positions
        if game["board_dimension"] ** 2 in f_positions.values():
            game_state = "finished"
        else:
            game_state = "progress"
        squares_traversed = {}
        for key in Player_Score.keys():
            squares_traversed[str(key)] = Player_Score[key]
        # print "\n",squares_traversed


        Send_data = {}

        Send_data["winner"] = Win_Stat
        Send_data["game_state"] = game_state
        Send_data["final_positions"] = f_positions
        Send_data["squares_traversed"] = squares_traversed
        # print Send_data
        json_data = json.dumps(Send_data)
        json_data = json_data + '\n'
        print json_data
        conn.send(json_data)


acceptor = socket.socket()
acceptor.bind(('0.0.0.0', int(sys.argv[1])))
acceptor.listen(3)


for i in range(3):
    pid = os.fork()


    if pid == 0:
        childpid = os.getpid()
        print "Child %s listening on localhost:9999" % childpid

        while 1:
            conns, addr = acceptor.accept()

            run(conns)


            print "Child is completed-->", childpid

os.wait()
print 'Server exiting....'
