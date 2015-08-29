from xbee import ZigBee
import serial
import struct

PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

def hex(bindata):
    return ''.join('%02x' % ord(byte) for byte in bindata)

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
xbee = ZigBee(ser,escaped=True)

# Continuously read and print packets
while True:
    try:
        response = xbee.wait_read_frame()
        print response
    except KeyboardInterrupt:
        break

ser.close()