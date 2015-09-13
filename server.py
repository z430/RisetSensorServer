#!/usr/bin/python

import select
import socket
import sys
import struct
import serial
from xbee import ZigBee
import binascii
from xbeeser import *

aports=0
aips=0
asensors=0
loop=0
#untuk pengiriman dengan data hingga 2^32 - 1 pada length

format = struct.Struct('!I')

"""
    Network Section
"""
def send(sock, message):
    sock.send(format.pack(len(message)) + message)

def file_read():
    translasi = file("translasi.txt", 'r')
    cols, indexToName = getColumns(translasi)
    translasi.close()
    aports=cols['PORT']
    aips=cols['IP']
    asensors=cols['SENSOR']
    return aports, aips, asensors

def getColumns(inFile, delim="\t", header=True):
    """
    Get columns of data from inFile. The order of the rows is respected
    :param inFile: column file separated by delim
    :param header: if True the first line will be considered a header line
    :returns: a tuple of 2 dicts (cols, indexToName). cols dict has keys that 
    are headings in the inFile, and values are a list of all the entries in that
    column. indexToName dict maps column index to names that are used as keys in 
    the cols dict. The names are the same as the headings used in inFile. If
    header is False, then column indices (starting from 0) are used for the 
    heading names (i.e. the keys in the cols dict)
    """
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
    return cols, indexToName
def serve(ports):

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
        # debugging sensor data value
        #print_status()

        # fetch data first before send it to client
        data_suhu = sensor_suhu()
        data_api = sensor_api()

        r, w, x = select.select(sockets, sockets, sockets)
        for sock in r:
            if sock in listeners:
                c, a = sock.accept()
                print(sock.getsockname(), ' <- ', a)
                aports, aips, asensors=file_read()
                dport=sock.getsockname()
                if int (dport[1]) == 2222:
                    #c.send(str('nilai sensor api:'))
                    c.send(str(data_api))
                elif int (dport[1]) == 2223:
                    #c.send(str('nilai sensor suhu:'))
                    c.send(str(data_suhu))
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