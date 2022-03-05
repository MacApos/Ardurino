#include <Servo.h>
#define pin 5

Servo servo0;
Servo servo1;
Servo servo2;
int pos0 = 0;
int pos1 = 0;
int pos2 = 0;

void setup()
{
  Serial.begin(9600);
  servo0.attach(5);
  servo1.attach(6);
  servo2.attach(7);
  
  servo0.write(0);
  servo1.write(0);
  servo2.write(0);
}

void loop()
{
  if (Serial.available() > 0){
    chart start = Serial.readStringUntil('\n');
    
    
  }
}