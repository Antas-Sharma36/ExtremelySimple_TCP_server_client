import socket

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host_name = socket.gethostname()
port = 444

serversocket.bind((host_name,port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()

    print("Recieved connection from" % str(address))

    message = "Thank you for connecting to the server" + "\r\n"  

    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
