import socket, struct, sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def recv_all(sock, length):
    data = ''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('socket closed %d bytes into a %d-byte message' % (len(data), length))
        data += more
    return data


def receive(sock):
    lendata = recv_all(sock, format.size)
    (length,) = format.unpack(lendata)
    return recv_all(sock, length)


def send(sock, message):
    sock.send(format.pack(len(message)) + message)

timeData = open("timestamp.txt", 'w')

if len(sys.argv) <= 2:
    print "This simple APP create by Sabrian"
    print "Usage ... send [IP ADDRESS] [PORT]"
else:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    format = struct.Struct('!I')  # untuk pengiriman dengan data hingga 2^32 - 1 pada length
    start_time = time.time()
    s.connect((HOST, PORT))
    send(s, 'HELLO')
    data = s.recv(4096)
    executeTime = time.time() - start_time
    print ("execution time: %s" % executeTime)
    timeData.write(str(executeTime))
    timeData.write("\n")
    timeData.close()
    s.close()
    #print data
