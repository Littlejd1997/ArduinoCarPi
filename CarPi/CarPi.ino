int RedPin;
int GreenPin;
int BluePin;
void setup() {
  pinMode(10, INPUT);
  pinMode(13, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  while (Serial.available() > 0) {
    switch (Serial.parseInt()) {
      case 0:
      {
        int pin = Serial.parseInt();
        int output = Serial.parseInt();
        if (Serial.read() == '\n') {
          analogWrite(pin, output);
        }
        break;
      }
      case 1:
      {
        RedPin = Serial.parseInt();
        GreenPin = Serial.parseInt();
        BluePin = Serial.parseInt();
        pinMode(RedPin,OUTPUT);
        pinMode(GreenPin,OUTPUT);
        pinMode(BluePin,OUTPUT);
        Serial.read();
        break;
      }
      case 2:{
        analogWrite(RedPin, Serial.parseInt());
        analogWrite(GreenPin, Serial.parseInt());
        analogWrite(BluePin, Serial.parseInt());
        Serial.read();
        break;
      }
    }
  }
}



