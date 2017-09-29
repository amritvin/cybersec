import socket

def Main():
    print("Send 'q' to exit\n")
    address = str(input("ip:port -> "))
    nick = raw_input("nick: ")

    try:
        if address.index(":") != 0:
            host = address[:address.index(":")]
            port = int(address[address.index(":")+1:])
    except ValueError:
        host = address
        port = 5000

    s = socket.socket()
    s.connect(("127.0.0.1", port))

    message = raw_input("-> ")

    while message != "q":
        s.send(bytes(message + "$" + nick, "UTF-8"))
        data = s.recv(1024)
        data = data.decode("UTF-8")
        data2 = data

        messageServer = str(data[:data.index("$")])
        nickServer = str(data[data.index("$")+1:])
        if not data == data2:
            print(nickServer + ": " + messageServer)
        message = input("-> ")
    s.close()

if __name__ == "__main__":
    Main()
