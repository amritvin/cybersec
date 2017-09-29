import socket

host = 'localhost'
port = 8060

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

while True:
    (client, address) = s.accept()
    print 'client connected'

    try:
        print recvall(client)
        client.sendall('hello client')
    finally:
        client.close()

