import binascii
import serial
from xbee import ZigBee


__author__ = 'myth'

#panjang dan tipe data menentukan cara pengiriman
#karena data sebenarnya dikirim dengan panjang 8bit
#jika lebih maka harus dipecah dan dikirim tiap 8 bit
#pin analog arduino mempunyai panjang 10bit

#rf data secara default menerima dalam bentuk ascii
#data sebenarnya dikirim dalam bentuk desimal kemudian diubah menjadi hex

def hex(bindata):
    return ''.join('%2x' % ord(byte) for byte in bindata)


def init_serial():
    port = '/dev/ttyUSB0'
    baud_rate = 9600
    ser = serial.Serial(port, baud_rate)
    return ser

xbee = ZigBee(init_serial(), escaped=True)

def explode_data():

    response = xbee.wait_read_frame()
    long_addr = hex(response['source_addr_long'][4:])
    rf_data = hex(response['rf_data'])

    return rf_data, long_addr

def sensor_api():
    data, alamat = explode_data()
    #print data, alamat
    if alamat  == '40b7a017':
        data_sensor = data
        return int(data_sensor, 16)

def sensor_suhu():
    data, alamat = explode_data()
    #print data, alamat
    if alamat == '40b3ec8a':
        data_suhu = data
        return int(data_suhu, 16)
