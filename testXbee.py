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
        datalength = len(rf)

        print shsa, int(rf, 16), rf, sa
    except KeyboardInterrupt:
        break

ser.close()

def request_data(self, addr_low, addr_high):
    self._addr_low = addr_low
    self._addr_high = addr_high
