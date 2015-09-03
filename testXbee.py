import binascii
from xbee import ZigBee
import serial
import struct

PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

def hex(bindata):
    return ''.join('%02x' % ord(byte) for byte in bindata)

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API objectmkk
xbee = ZigBee(ser,escaped=True)

# Continuously read and print packets
while True:
    try:
        response = xbee.wait_read_frame()
        sa = hex(response['source_addr_long'][4:])
        rf = hex(response['rf_data'])
        shsa = hex(response['source_addr'])
        #rf = hex(response['rf_data'][0:4])[1]
        datalength = len(rf)
        #h = struct.unpack('f',response['rf_data'][4:])[0]
        #if datalength == 16:
         #   t = struct.unpack('0', response['rf_data'][0:4])
        #    print t
        s = binascii.a2b_hex(rf)
        print sa, rf, datalength, s, shsa
        print response
    except KeyboardInterrupt:
        break

ser.close()

def request_data(self, addr_low, addr_high):
    self._addr_low = addr_low
    self._addr_high = addr_high
