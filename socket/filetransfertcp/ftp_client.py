# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 07:10:59 2022

@author: souvi
"""

import socket
import sys
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost',10000)
client.connect(server_address)

file_name = client.recv(1000).decode()
file_name = "new" + file_name
file = open(file_name,"wb")
data = client.recv(10000)
file.write(data)

file.close()
client.close()
