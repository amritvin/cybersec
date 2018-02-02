#!/usr/bin/python           # This is server.py file
"""
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12329              # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   msg=raw_input("ENTER YOUR MESSAGE  :")
   c.send(msg)
   print c.recv(1024)
   c.close()                # Close the connection
"""
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 8169)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
	    #print "CLIENT :  "

             #print('received {!r}'.format(data))
            data=raw_input("ENETR MESSAGE: ")
            print('sending . . .',data)
            connection.sendall(data)
            print client_address
            print connection.recv(2024)

    finally :
     	connection.close()
