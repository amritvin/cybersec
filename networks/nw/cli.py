import socket
#s = socket.create_connection(('localhost', 8060))
#s = socket.create_connection((args.ip, args.port))
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 8000 
s.connect((host, port))
try:
    s.sendall('hello server')
    print recvall(s)
finally:
    s.close()
