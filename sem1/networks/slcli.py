
import socket
import sys
import json

# Create a TCP/IP socket

ipaddr=sys.argv[1]
port=int(sys.argv[2])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (ipaddr, port)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
con=True
res={}
try:
    while(con):
    # Send data
    	#message =raw_input("Enter message to server")
    	#print('sending {!r}'.format(message))
    # Look for the response
    	#amount_received = 0
    	#amount_expected = 1024
        #while amount_received < amount_expected:
        data=raw_input("enter: ")
        res=json.loads(data.strip())
        r=json.dumps(res)
        sock.sendall(r)
        data = sock.recv(1024)
        #print r
        print data
        #amount_received += len(data)
       	#print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
