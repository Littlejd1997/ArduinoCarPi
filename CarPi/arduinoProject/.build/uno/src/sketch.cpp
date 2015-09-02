#include <Arduino.h>

void setup();
void loop();
#line 1 "src/sketch.ino"
int RedPin;
int GreenPin;
int BluePin;
bool rpiON = false;
void setup() {
  pinMode(10, INPUT);
  pinMode(13, OUTPUT);
  pinMode(0,OUTPUT);
  pinMode(2, INPUT);
  Serial.begin(115200);
}

void loop() {
  if (digitalRead(2) == HIGH && rpiON){
    digitalWrite(0,HIGH);
  }else if (digitalRead(2) == LOW && !rpiON){
    digitalWrite(0,LOW);
  }
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



