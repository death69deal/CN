# crc receiver
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("TCP CLIENT SOCKET CREATED")
ip = socket.gethostbyname(socket.gethostname())
port = 8080
s.connect((ip, port))
print("CONNECTION ESTABLISHED")


data = s.recv(1024).decode()
print ("Data recived : ",data)
divisor = "1101"

p = len(divisor)

divident = data

tmp = divident[0: p]


def xor(a, b):
    result = []

    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


while p < len(divident):

    if tmp[0] == '1':

        tmp = xor(divisor, tmp) + divident[p]

    else:

        tmp = xor('0' * p, tmp) + divident[p]

    p += 1

if tmp[0] == '1':
    tmp = xor(divisor, tmp)
else:
    tmp = xor('0' * p, tmp)

checkword = tmp
print('the checkword:', checkword)

if (int(checkword, 2) == 0):
    print('The data is error free:')

else:
    print('The data is error aded:')