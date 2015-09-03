#include <XBee.h>

#define ARRAY_SIZE 4
/* XBee Setting

 *  NODE_KELEMBAPAN
 *  PAN ID = 1AAA
 *  SH = 13A200
 *  SL = 40B7A017
  
 *  NODE_SUHU
 *  PAN ID = 1AAA
 *  SH = 13A200
 *  SL = 40B7A017

 *  COORDINATOR ADDRESS
 *  SH = 13A200
 *  SL = 40A62ADA


*/

// create the XBee object
XBee xbee = XBee();

int pinData = 200;

uint8_t payload[] = {'h','e','l','l','o', 'o', 'o'};

// SH + SL Address of receiving XBee
XBeeAddress64 addr64 = XBeeAddress64(0x0013a200, 0x40a62ada);
ZBTxRequest zbTx = ZBTxRequest(addr64, payload, sizeof(payload));

// Try using 16 bit address
//Tx16Request tx = Tx16Request(0x0000, payload, sizeof(payload));

ZBTxStatusResponse txStatus = ZBTxStatusResponse();

int pin5 = 0;

int statusLed = 13;
int errorLed = 12;

void flashLed(int pin, int times, int wait) {

  for (int i = 0; i < times; i++) {
    digitalWrite(pin, HIGH);
    delay(wait);
    digitalWrite(pin, LOW);

    if (i + 1 < times) {
      delay(wait);
    }
  }
}

void setup() {
  pinMode(statusLed, OUTPUT);
  pinMode(errorLed, OUTPUT);

  Serial.begin(9600);
  xbee.setSerial(Serial);
}

void loop() {   
  // break down 10-bit reading into two bytes and place in payload

  xbee.send(zbTx);
  delay(100);
  // flash TX indicator
  
}