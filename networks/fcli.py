import socket,sys

def client():
    host="127.0.0.1"
    port=int(sys.argv[1])
    s=socket.socket()
    s.connect((host, port))
    m=raw_input("Enter your NICK NAME:")
    msg=raw_input(":")
    msg=m+" : "+msg
    #encoded_msg=bytes(msg, "utf-8")

    while msg!='q':
    #        print encoded_msg
            s.send(msg)
            msg=raw_input(":")
            msg=m+" : "+msg
    #        encoded_msg=bytes(msg, "utf-8")
            data=s.recv(1024)
            print data

client()
