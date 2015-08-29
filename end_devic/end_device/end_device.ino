#include <XBee.h>

#define ARRAY_SIZE 4
/* XBee Setting
 *  PAN ID = 1222
 *  SC = 7FFF
 *  AP = 2
 *  SH = 13A200
 *  SL = 40B7A017
 *  COORDINATOR ADDRESS
 *  SH = 13A200
 *  SL = 40A62ADA
*/

// Create the XBee Object
XBee xbee = XBee();

uint8_t payload[ARRAY_SIZE];

union u_tag{
	uint8_t b[4];
	float fval;
} u;

// SH + SL Address of receiving XBee
XBeeAddress64 addr64 = XBeeAddress64(0x00000000, 0x00000000);
ZBTxRequest zbTx = ZBTxRequest(addr64, payload, sizeof(payload));
ZBTxStatusResponse txStatus = ZBTxStatusResponse();

int statusLed = 13;
int errorLed = 12;

void flashLed(int pin, int times, int wait){
	for (int i = 0; i < times; i++){
		digitalWrite(pin, HIGH);
		delay(wait);
		digitalWrite(pin, LOW);

		if(i + 1 < times){
			delay(wait);
		}
	}
}

void setup(){
	pinMode(statusLed, OUTPUT);
	pinMode(errorLed, OUTPUT);

	Serial.begin(9600);
	xbee.setSerial(Serial);
}

void loop(){

	payload[0] = 'H';
  	payload[1] = 0x7E;
	payload[2] = 0x11;
  	payload[3] = 0x13;
  	payload[4] = 0x7D;

	xbee.send(zbTx);

	// flash tx indicator
	flashLed(statusLed, 3, 100);

	// after sending a tx request, we expect a status response
	// wait up to half second for the status response
	if(xbee.readPacket(500)){
		// got response

		// should be a znet tx status
		if(xbee.getResponse().getApiId() == ZB_TX_STATUS_RESPONSE){
			xbee.getResponse().getZBTxStatusResponse(txStatus);

			// get the delivery status, the fifth byte
			if(txStatus.getDeliveryStatus() == SUCCESS){
				flashLed(statusLed, 5, 500);
			} else {
				flashLed(errorLed, 3, 500);
			}
		}
	}

	else if(xbee.getResponse().isError()){
	    
	}
	else {
		flashLed(errorLed, 4, 150);
	}

	delay(500);

}