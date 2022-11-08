import socket
IP='127.0.0.1'
port=20001
buffersize=1024
msgFromClient="client responded"
bytesToSend=str.encode(msgFromClient)
UDP_ClientSocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
UDP_ClientSocket.sendto(bytesToSend, (IP,port))
msgFromServer=UDP_ClientSocket.recvfrom(buffersize)
msg="message from server {}".format(msgFromServer[0])
print(msg)