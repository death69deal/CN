import socket
BUFFER_SIZE = 4096
s = socket.socket()
print("Connecting to 127.0.0.1:5001")
s.connect(("127.0.0.1", 5001))
print("Connected to Server Terminal")
while True:
 command = input("\nServer>> ")
 s.sendall(command.encode())
 if command == 'exit':
     break
print("Closing remote connection with Server")
s.close()