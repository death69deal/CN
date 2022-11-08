import socket 
s=socket.socket()
host=""
port=5000
s.connect(("127.0.0.1",9090))
with open('recieved-file.txt','wb')as f:
    print('file opened')
    while True:
        print('recieving data.....')
        data=s.recv(1024)
        if not data:
            break
        f.close()
        print('successfully got the file')
        s.close()
        print('connection closed')
        