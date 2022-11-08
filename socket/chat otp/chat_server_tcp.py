# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:40:13 2022

@author: souvik
"""

import socket
import sys
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost',10000)
server.bind(server_address)
server.listen(1)


print("Waiting for the connection...")
connection,client_address = server.accept()


pasw = input("Set OTP:")
otp = connection.recv(1000).decode()
if pasw == otp:
    q = "success"
    connection.sendall(q.encode())
    print("Connection established with",client_address)
    
    message = ""
    while message!='end':
        data = connection.recv(1000).decode()
        if data:
            print("Client:",data)
            message = input("Server: ")
            connection.sendall(message.encode())
        else:
            break;

else:
    m = "Error"
    connection.sendall(m.encode())
        
connection.close()
server.close()