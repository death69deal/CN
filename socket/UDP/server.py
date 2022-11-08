import socket
localIP='127.0.0.1'
localport=20001
buffersize=1024
msgFromServer="server responded"
bytesToSend=str.encode(msgFromServer)
UDP_ServerSocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
UDP_ServerSocket.bind((localIP,localport))
print("UDP server up and listening")
while True:
    bytesAddresspair=UDP_ServerSocket.recvfrom(buffersize)
    message=bytesAddresspair[0]
    address=bytesAddresspair[1]
    clientMsg="Message from clint: {}".format(message)
    clientIP="clientIP Address: {}".format(address)
    print(clientMsg)
    print(clientIP)
    UDP_ServerSocket.sendto(bytesToSend, address)
