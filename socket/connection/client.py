import socket
import sys
import time
socket_server=socket.socket()
server_host=socket.gethostname()
ip=socket.gethostbyname(server_host)
sport=8080
server_host=input("Enter friends ip address")
name=input("enter friends name")
socket_server.connect((server_host,sport))
socket_server.send(name.encode())
server_name=socket_server.recv(1024)
server_name=server_name.decode()
print(server_name,'has joined......')
while True:
    message=(socket_server.recv(1024)).decode()
    print(server_name,':',message)
    message=input("me")
    socket_server.send(message.encode())