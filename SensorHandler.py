from xbee import XBee
import serial, time, datetime, sys

class SensorHandler:

    def __init__(self):
        print "init"
        #SERIALPORT = "/dev/ttyUSB0"
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