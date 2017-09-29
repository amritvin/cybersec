import socket
import sys
import json
from threading import Thread

connection= socket.socket()
host = "0.0.0.0"
port = 9999
count =1
data = {
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

json_data =json.dumps(data)
connection.connect((host, port))

# noinspection PyUnboundLocalVariable
class ClientThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        #self.count=0



    def run(self):
        print self.getName(),"Starting New Thread"
        count=0
        while True:

            print count
            if count >=1:
                print self.getName(),"sendding 0"
                connection.send("0" + '\n')
                break

            print "Repeating the  Thread",self.getName()

            connection.send(json_data + '\n')
            #print json_data
            dataRecvd = connection.recv(999999)
            data = json.loads(dataRecvd.strip())
            print self.getName(),data
            count= count+ 1


threads = []
count1= 0
while True:
    if count1 >=3:
        break
    newthread = ClientThread()
    newthread.start()
    threads.append(newthread)
    count1 = count1 +1







for t in threads:
    t.join()


connection.close()
