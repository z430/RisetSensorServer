import select
import socket
import sys
import struct
from SensorHandler import *

#global declaration port, ip, sensor_name
aports = 0
aips = 0
asensor = 0

#Untuk pengiriman data hingga 2^32 - 1 pada length
formatData = struct.Struct('!I')

#send handler
def send(sock, message):
    sock.send(formatData.pack(len(message)) + message)

#get colomns name on translation file
def getColumns(inFile, delim="\t", header=True):
    cols = {}
    indexToName = {}
    for lineNum, line in enumerate(inFile):
        if lineNum == 0:
            headings = line.split(delim)
            i = 0
            for heading in headings:
                heading = heading.strip()
                if header:
                    cols[heading] = []
                    indexToName[i] = heading
                else:
                    # in this case the heading is actually just a cell
                    cols[i] = [heading]
                    indexToName[i] = i
                i += 1
        else:
            cells = line.split(delim)
            i = 0
            for cell in cells:
                cell = cell.strip()
                cols[indexToName[i]] += [cell]
                i += 1
    return cols

#read the translasition file
def file_read():
    translasi = file("translasi.txt", 'r')
    cols = getColumns(translasi)
    translasi.close()
    aports = cols['PORT']
    aips = cols['IP']
    asensor = cols['SENSOR']
    return aports, aips, asensor

#request handler
def serve(ports):
    baca_sensor = SensorHandler()
    listeners, sockets = [], []
    for port in ports:
        listener = socket.socket()
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind(('127.0.0.1', port))
        listener.setblocking(False)
        listener.listen(5)
        listeners.append(listener)
        sockets.append(listener)
        print(listener.getsockname(), ' listening')
    while True:
        r, w, x = select.select(sockets, sockets, sockets)
        for sock in r:
            if sock in listeners:
                c, a = sock.accept()
                print(sock.getsockname(), ' <- ', a)
                aports, aips, asensors=file_read()
                dport=sock.getsockname()
                if int (dport[1]) == 2222:
                    pesan = baca_sensor.api()
                    c.send(str(pesan))
                elif int (dport[1]) == 2223:
                    baca_sensor.suhu()
                    c.send('Nih data suhunya')
                sockets.append(c)
            else:
                buf = sock.recv(80)
                if not buf:
                    print(sock.getpeername(), ' EOF')
                    sockets.remove(sock)
                else:
                    print(sock.getpeername(), ' <- ', buf)
        for sock in w:
            pass
        for sock in x:
            print(sock.getpeername(), ' error')
            sockets.remove(sock)

if __name__ == '__main__':

    translasi = file("translasi.txt", 'r')
    cols, indexToName = getColumns(translasi)
    translasi.close()
    #serve(cols['PORT'],cols['SENSOR'])
    serve (int(arg) for arg in cols['PORT'])
    #serve(int(arg) for arg in sys.argv[1:])