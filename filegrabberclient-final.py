import socket

mysocket = socket.socket()
mysocket.connect(("18.207.213.126", 8000))
while True:
    print(mysocket.recv(2048).decode())
