import os, socket,sys
bst= " "
host="0.0.0.0"
port=int(sys.argv[1])
s=socket.socket()
s.bind((host, port))
s.listen(10)
arr=[]
msh=[]
def sendchat(sk,person):
    print msh
    sk.send(msh[person-1])
def handle_client(s, addr, i):
    global msh
    ind=0
    while True:
        data=s.recv(1024)
        data=data+"\n"
        decoded_data=data.decode("utf-8")
        if not decoded_data:
                print("\nconnection wiarr.append(c)th client " + str(i) + " broken\n")
                break
        print("  CLIENT " + str(i) + " -> " + decoded_data,addr)
        msh.append(data +"&")
        sendchat(s,i)
        ind=ind+1

def server():
    i=1
    while i<=10:
        c, addr=s.accept()
        child_pid=os.fork()
        if child_pid==0:
                arr.append(c)
                print("\nconnection successful with client " + str(i) + str(addr) + "\n")
                handle_client(c, addr, i)
        else:
                i+=1

server()
