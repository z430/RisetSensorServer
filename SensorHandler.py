from xbee import XBee
import serial, time, datetime, sys

# END_DEVICE_1
# Serial High (SH) : 13A200
# Serial Low  (SL) : 40B7A017
#
# COORDINATOR
# SH : 13A200
# SL : 40A62ADA

class SensorHandler:

    # node 16 bit MY address


    def __init__(self):
        print "init"
        SERIALPORT = "/dev/ttyUSB0"
    #BAUDRATE = 9600
    #self.ser = serial.Serial(SERIALPORT, BAUDRATE)
    #print self.ser
    #self.xbee = XBee(self.ser)
    #print "initialize complete"

    def suhu(self):
        print "suhu sekarang"

    def api(self):
        print "api:"

    def test_data(self):
        #response = self.xbee.wait_read_frame()
        print "Lontong"