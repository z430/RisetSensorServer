from xbee import ZigBee
import serial, time, datetime, sys
import binascii


class SensorHandler:

    """
        Node Address:
            1.  SH = 13A200
                SL = 40B3EC8A
            2.  SH = 13A200
                SL = 40B7A017
    """
    #PORT = '/dev/ttyUSB0'
    #BAUD_RATE = 9600

    def __init__(self):
        self.port = '/dev/ttyUSB0'
        self.baud_rate = 9600
        self.ser = serial.Serial(self.port, self.baud_rate)
        self.xbee = ZigBee(self.ser, escaped=True)

    def explode_data(self):
        self.response = self.xbee.wait_read_frame()
        self.long_addr = hex(self.response['source_addr_long'][4:])
        self.rf_data = hex(self.response['rf_data'])
        self.data_length = len(self.rf_data)

    def suhu(self):
        if self.long_addr == '40b3ec8a':
            data_readable = binascii.a2b_hex(self.rf_data)
            return data_readable

    def api(self):
        print "api:"
