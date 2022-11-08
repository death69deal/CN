# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:32:36 2022

@author: souvik
"""

import socket
import sys
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost',10000)
client.connect(server_address)


otp = input("Enter OTP:")
client.send(otp.encode())
e = "Error"
s = "success"
z = client.recv(1000).decode()


if e == z:
    print("Wrong OTP...RETRY")
    client.close()
    
elif s == z:
    print("Connecting to port:",server_address)
    
    
    message = input("Client: ")
    client.sendall(message.encode())
    
    
    while message!='end':
        data = client.recv(1000).decode()
        if data:
            print("Server: ",data)
            message = input("Client: ")
            client.sendall(message.encode())
        else:
            break;
            
            
    client.close()