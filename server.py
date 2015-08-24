import select
import socket
import sys
import struct

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
    listeners, socket = [], []
    for port in ports:
        listener 

if __name__ == '__main__':
    file_read()
