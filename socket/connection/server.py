import socket
import sys
import time
new_socket=socket.socket()
host_name=socket.gethostname()
s_ip=socket.gethostbyname(host_name)
port=8080
new_socket.bind((host_name,port))
name=input("Enter name: ")
new_socket.listen(1)
conn,add=new_socket.accept()
print("receved connection from",add[0])
print("connection estabilished from",add[0])
client=(conn.recv(1024)).decode()
conn.send(name.encode())
while True:
    message=input("me")
    conn.send(message.encode())
    message=conn.recv(1024)
    message=message.decode()
    print(client,':',message)
    