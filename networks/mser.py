import socket
import time
import os
from threading import Thread

folderPath = "Chat Logs"
filePath = folderPath + "/" + str(time.strftime("%H-%M-%S_%d-%m-%Y")) + ".txt"

def clientHandler(c):
    while True:
        data = c.recv(1024)
        if not data:
            break

    data = data.decode("UTF-8")
    message = str(data[:data.index("$")])
    nick = str(data[data.index("$")+1:])
    print(nick + ": " + message)
    saveChat(nick, message)
    print("   Sending: " + data)
    c.send(bytes(data, "UTF-8"))
    c.close()

def saveChat(nick, message):
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    if not os.path.exists(filePath):
        f = open(filePath, "a")
        f.close()

    f = open(filePath, "a")
    f.write(nick + ": " + message + "\n")
    f.close()

def Main():
    host = str(socket.gethostbyname(socket.gethostname()))
    port = 5000
    print(host + ":" + str(port) + "\n")
    Clients = int(input("Clients: "))
    s = socket.socket()
    s.bind(("0.0.0.0", port))
    s.listen(Clients)
    for i in range(Clients):
        c, addr = s.accept()
        print("Connection from: " + str(addr))

        Thread(target=clientHandler(c)).start()
    s.close()

if __name__ == "__main__":
    Main()
