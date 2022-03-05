#include <Servo.h>
#define pin 5

Servo servo;
int pos = 0;
int add = 10;

void setup()
{
  Serial.begin(9600);
  servo.attach(pin);
}

void loop()
{
  while (pos < 180) {
    Serial.println(pos);
  	servo.write(pos);
    pos = pos + add;
    delay(1000);
  }
  while (pos > 0) {
    Serial.println(pos);
  	servo.write(pos);
    pos = pos - add;
    delay(1000);
  }
}