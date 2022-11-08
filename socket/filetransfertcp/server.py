import socket
port=5000
s=socket.socket()
host=""
s.bind(("127.0.0.1",9090))
s.listen(1)
print('server listening....')
while True:
    conn,addr=s.accept()
    print('got connection from:', addr)
    data=conn.recv(1024)
    print('server recieved',repr(data))
    filename='hello.txt'
    f=open(filename,'rb')
    l=f.read(1024)
    while True:
        conn.send(1)
        print('send',repr(1))
        l=f.read(1024)
        f.close()
        print('Done sending')
        conn.send('Thankyou for connecting. Eibar vote jeete k raja da abr k')
        conn.close()
    