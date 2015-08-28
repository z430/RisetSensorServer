#define ARRAY_SIZE 3

String dataPayload[ARRAY_SIZE];
char dumpData;
int ledTx = 13;

void setup() {
  Serial.begin(9600);
  dumpData = '}';
  pinMode(ledTx, OUTPUT);
}

void loop() {
/*
 * Dump Test Data
  dataPir = 'w';
  dataPayload[0] = readPir();
  dataPayload[1] = dataPir;
  dataPayload[2] = readSuhu();
  Serial.print(char(dataPayload[0]));
  Serial.print(dataPayload[0]);
  Serial.print(dataPir);
*/
  dataPayload[0] = "}";
  dataPayload[1] = String(readPir());
  dataPayload[2] = String(readSuhu());

  for(int i=0;i<ARRAY_SIZE;i++)
  {
    Serial.print(dataPayload[i]);  
    //Serial.println(dumpData);
    digitalWrite(ledTx,HIGH);
    delay(100);
    digitalWrite(ledTx,LOW);
  }
  
  //delay(500);
  
}

int readPir(){
  int data;
  data = 9;

  return data;
}

int readSuhu(){
  int data;
  data = 2;

  return data;
}
